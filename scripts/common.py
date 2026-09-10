"""Shared helpers for the bias red-team lab scripts.

Every script in this folder imports from here so the conversation-running
and tracing logic (LangSmith `traceable` wrapping) lives in exactly one
place instead of being copy-pasted per category.
"""

import os

from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langsmith import traceable

load_dotenv()

DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")


def get_model(model_name: str = DEFAULT_MODEL, temperature: float = 0.7) -> ChatOpenAI:
    """Return a chat model instance. Requires OPENAI_API_KEY to be set."""
    return ChatOpenAI(model=model_name, temperature=temperature)


def make_conversation_runner(run_name: str, tags: list[str]):
    """Build a function that runs a multi-turn conversation as ONE traced
    LangSmith run (with each model call nested underneath it as a child
    run), instead of one disconnected top-level run per turn.

    Usage:
        runner = make_conversation_runner(run_name="ageism-adversarial", tags=["ageism"])
        history = runner(model, system_prompt, [turn1, turn2, turn3, turn4])
    """

    @traceable(name=run_name, tags=tags, run_type="chain")
    def _run(model: ChatOpenAI, system_prompt: str, turns: list[str]) -> list:
        history = [SystemMessage(content=system_prompt)]
        for i, user_turn in enumerate(turns, start=1):
            history.append(HumanMessage(content=user_turn))
            print(f"\n--- Turn {i} ---")
            print(f"HUMAN: {user_turn}")
            response = model.invoke(history)
            history.append(AIMessage(content=response.content))
            print(f"MODEL: {response.content}")
        return history

    return _run
