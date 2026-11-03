"""Main entry point and demonstration runner for the LangGraph University Assistant."""

import os
import sys
from getpass import getpass
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

from src.graph import build_assistant_graph


def get_llm():
    """Initializes the LLM instance with user API key from env or prompt."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        if sys.stdin.isatty():
            api_key = getpass("Enter your OpenAI API key: ").strip()
            os.environ["OPENAI_API_KEY"] = api_key
        else:
            print("Warning: OPENAI_API_KEY not found in environment.")
    return ChatOpenAI(model="gpt-4o-mini", temperature=0)


def run_demonstration(assistant):
    """Runs tests across all categories, tools, memory, and error cases."""
    print("=" * 70)
    print("LangGraph Capstone Assistant - Demonstration")
    print("=" * 70)

    demo_queries = [
        ("What topics are covered in a machine learning course?", "demo-session"),
        ("Write a Python function to check if a word is a palindrome.", "demo-session"),
        ("What is 125 * 38 + 17?", "demo-session"),
        ("How do I request an official enrollment certificate?", "demo-session"),
        ("What is today's date?", "demo-session"),
        ("   ", "demo-session"),  # Empty input test
    ]

    for question, thread_id in demo_queries:
        config = {"configurable": {"thread_id": thread_id}}
        print(f"\n[USER]     : {question!r}")
        result = assistant.invoke({"messages": [HumanMessage(content=question)]}, config)
        print(f"[CATEGORY] : {result.get('category')}")
        print(f"[ASSISTANT]: {result['messages'][-1].content}")

    # Memory Persistence Verification
    print("\n" + "=" * 70)
    print("Testing Multi-Turn Conversational Memory (Same thread_id)")
    print("=" * 70)
    mem_config = {"configurable": {"thread_id": "student-ahmed"}}

    print("\nTurn 1: Telling name...")
    r1 = assistant.invoke({"messages": [HumanMessage(content="Hello, my name is Ahmed.")]}, mem_config)
    print(f"[ASSISTANT]: {r1['messages'][-1].content}")

    print("\nTurn 2: Asking for recalled name...")
    r2 = assistant.invoke({"messages": [HumanMessage(content="What is my name?")]}, mem_config)
    print(f"[ASSISTANT]: {r2['messages'][-1].content}")

    print("\nTurn 3: Asking in a DIFFERENT thread (isolated memory)...")
    other_config = {"configurable": {"thread_id": "student-other"}}
    r3 = assistant.invoke({"messages": [HumanMessage(content="What is my name?")]}, other_config)
    print(f"[ASSISTANT]: {r3['messages'][-1].content}")


def main():
    try:
        llm = get_llm()
        assistant = build_assistant_graph(llm)
        run_demonstration(assistant)
    except Exception as e:
        print(f"Error during execution: {e}")


if __name__ == "__main__":
    main()

