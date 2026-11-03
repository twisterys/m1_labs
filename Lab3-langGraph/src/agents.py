"""Agent definitions, prompts, classification, and fallback logic."""

from typing import Dict, Any, Callable
from langchain_core.messages import SystemMessage, AIMessage
from src.state import AssistantState

CATEGORIES = [
    "COURSES",
    "PROGRAMMING",
    "MATHEMATICS",
    "ADMINISTRATION",
    "GENERAL",
]

NODE_NAMES = {c: f"{c.lower()}_agent" for c in CATEGORIES}

SYSTEM_PROMPTS: Dict[str, str] = {
    "COURSES": (
        "You are a university courses advisor. Explain course content, prerequisites, "
        "schedules, and study strategies. If you lack institution-specific data, say so honestly."
    ),
    "PROGRAMMING": (
        "You are a programming tutor. Give clear, concise explanations and correct, "
        "idiomatic Python code with explanations when appropriate."
    ),
    "MATHEMATICS": (
        "You are a mathematics tutor. Provide clear step-by-step reasoning. "
        "ALWAYS use the calculator tool for arithmetic and numerical computations."
    ),
    "ADMINISTRATION": (
        "You are a university administration assistant (enrollment, tuition fees, "
        "certificates, academic procedures, and deadlines). Never invent official rules "
        "or deadlines; recommend contacting the administration office when unsure."
    ),
    "GENERAL": (
        "You are a helpful university assistant. Use the date/time tool for questions "
        "about the current date or time."
    ),
}


def build_classifier(llm: Any) -> Callable[[AssistantState], Dict[str, Any]]:
    """Factory returning a classification node equipped with error handling."""

    def classify(state: AssistantState) -> Dict[str, Any]:
        last = state["messages"][-1]
        text = (last.content if hasattr(last, "content") else str(last)).strip()

        # Error handling 1: Empty input
        if not text:
            return {"category": "EMPTY"}

        prompt = f"""
        Classify the student's question into exactly one category:
        COURSES (course content, syllabus, schedules, exams, grading),
        PROGRAMMING, MATHEMATICS,
        ADMINISTRATION (enrollment, fees, certificates, procedures, deadlines),
        GENERAL (anything else).

        Question: {text}

        Return only the category name in capital letters.
        """
        try:
            raw = llm.invoke(prompt).content.strip().upper()
        except Exception as e:
            # Error handling 2: API error during classification
            return {"category": "ERROR"}

        # Error handling 3: Unknown or multi-word output -> Match known label or fallback
        category = next((c for c in CATEGORIES if c in raw), "GENERAL")
        return {"category": category}

    return classify


def make_agent(category: str, llm_with_tools: Any) -> Callable[[AssistantState], Dict[str, Any]]:
    """Builds a specialized agent node with its domain prompt and error recovery."""
    system = SystemMessage(content=SYSTEM_PROMPTS[category])

    def node(state: AssistantState) -> Dict[str, Any]:
        try:
            response = llm_with_tools.invoke([system] + state["messages"])
            return {"messages": [response]}
        except Exception as e:
            # Error recovery for agent execution
            return {
                "messages": [
                    AIMessage(
                        content=(
                            f"I encountered a technical problem while generating the answer "
                            f"({type(e).__name__}). Please retry your request."
                        )
                    )
                ]
            }

    return node


def fallback_node(state: AssistantState) -> Dict[str, Any]:
    """Graceful fallback for empty input or classification failures."""
    cat = state.get("category", "")
    if cat == "EMPTY":
        msg = "Your question seems empty. Please type a question and I'll be happy to help!"
    else:
        msg = "Sorry, I couldn't process your request right now. Please try again in a moment."
    return {"messages": [AIMessage(content=msg)]}

