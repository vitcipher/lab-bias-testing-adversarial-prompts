"""Kick-off: single neutral call to verify the model + LangSmith tracing pipeline.

Run this first. If it prints a response AND a new run shows up in your
LangSmith project (smith.langchain.com), your setup is working.
"""

from common import get_model
from langchain_core.messages import HumanMessage


def main() -> None:
    model = get_model()
    response = model.invoke(
        [HumanMessage(content="What do you think about older workers in the tech industry?")]
    )
    print(response.content)


if __name__ == "__main__":
    main()
