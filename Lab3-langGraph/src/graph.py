"""LangGraph graph assembly and compilation for the Capstone Assistant."""

from typing import Any
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langgraph.checkpoint.memory import MemorySaver

from src.state import AssistantState
from src.tools import ALL_TOOLS
from src.agents import (
    CATEGORIES,
    NODE_NAMES,
    build_classifier,
    make_agent,
    fallback_node,
)


def route_after_classifier(state: AssistantState) -> str:
    """Routes to the relevant specialized agent node or fallback."""
    cat = state.get("category", "GENERAL")
    return NODE_NAMES.get(cat, "fallback")


def route_after_agent(state: AssistantState) -> str:
    """Inspects the last message to decide whether tools need to be called."""
    last = state["messages"][-1]
    if getattr(last, "tool_calls", None):
        return "tools"
    return END


def route_after_tools(state: AssistantState) -> str:
    """Returns control back to the specific specialized agent that initiated the tool call."""
    cat = state.get("category", "GENERAL")
    return NODE_NAMES.get(cat, "general_agent")


def build_assistant_graph(llm: Any, checkpointer: Any = None):
    """Assembles and compiles the full Capstone Assistant workflow graph."""
    if checkpointer is None:
        checkpointer = MemorySaver()

    # Bind tools to the LLM
    llm_with_tools = llm.bind_tools(ALL_TOOLS)

    # Initialize graph builder
    builder = StateGraph(AssistantState)

    # Add core infrastructure nodes
    builder.add_node("classifier", build_classifier(llm))
    builder.add_node("fallback", fallback_node)
    builder.add_node("tools", ToolNode(ALL_TOOLS, handle_tool_errors=True))

    # Add specialized category agent nodes
    for c in CATEGORIES:
        builder.add_node(NODE_NAMES[c], make_agent(c, llm_with_tools))

    # Set up edges
    builder.add_edge(START, "classifier")

    # Routing from classifier
    classifier_branches = {**{name: name for name in NODE_NAMES.values()}, "fallback": "fallback"}
    builder.add_conditional_edges("classifier", route_after_classifier, classifier_branches)

    # Routing after agent execution (tool loop or finish)
    for c in CATEGORIES:
        builder.add_conditional_edges(
            NODE_NAMES[c],
            route_after_agent,
            {"tools": "tools", END: END},
        )

    # Routing from tools back to the calling agent
    tools_branches = {name: name for name in NODE_NAMES.values()}
    builder.add_conditional_edges("tools", route_after_tools, tools_branches)

    # Fallback finishes execution
    builder.add_edge("fallback", END)

    # Compile with persistence
    compiled_app = builder.compile(checkpointer=checkpointer)
    return compiled_app

