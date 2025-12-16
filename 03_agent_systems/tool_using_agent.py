# combined_calculator_tool.py

import logging
from typing import Type
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

from langchain.tools import BaseTool
from langchain.agents import create_agent
from langchain.messages import HumanMessage

from langchain_google_genai import ChatGoogleGenerativeAI

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Input Schema for the Multiply Tool
class MultiplyInput(BaseModel):
    a: int = Field(..., description="First number")
    b: int = Field(..., description="Second number")

# Multiply Tool
class MultiplyTool(BaseTool):
    name: str = "multiply"
    description: str = "Multiply two integers"
    args_schema: Type[BaseModel] = MultiplyInput

    def _run(self, a: int, b: int) -> int:
        result = a * b
        logger.info(f"[MultiplyTool] {a} * {b} = {result}")
        return result

    async def _arun(self, a: int, b: int) -> int:
        return self._run(a, b)

# Main
if __name__ == "__main__":
    # Initialize Gemini via the google-genai integration
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

    # Create the agent
    agent = create_agent(
        model=llm,
        tools=[MultiplyTool()],
        system_prompt="You are a helpful assistant that uses the multiply tool when needed.",
    )

    # Must include a user message in a messages list
    messages = [
        HumanMessage(content="Multiply 12 and 8")
    ]

    # Invoke the agent
    response = agent.invoke({"messages": messages})

    # The last message in the agent response will contain the result
    print("Agent Response:", response["messages"][-1].content)