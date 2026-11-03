"""State definitions for the LangGraph agent workflows."""

from typing import TypedDict, Annotated, List, Any
from langgraph.graph.message import add_messages


class SimpleAgentState(TypedDict):
    """Basic state used for introductory 1-2 node workflows."""
    message: str
    response: str


class TwoStageState(TypedDict):
    """State for analyzer -> generator two-stage pipeline."""
    question: str
    analysis: str
    answer: str


class RouterState(TypedDict):
    """State for multi-branch conditional routing."""
    question: str
    category: str
    answer: str


class AssistantState(TypedDict):
    """State for the Capstone Intelligent University Assistant.

    Attributes:
        messages: An appended sequence of chat messages managed via add_messages reducer.
        category: The classification label assigned to the user query.
    """
    messages: Annotated[List[Any], add_messages]
    category: str

