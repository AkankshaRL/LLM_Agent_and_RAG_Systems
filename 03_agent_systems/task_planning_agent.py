import datetime
import logging
from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage

# ----------------------------
# Logging
# ----------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ----------------------------
# Define Tools
# ----------------------------

@tool
def get_current_date() -> str:
    """Returns today's date for deadline calculation."""
    today = datetime.date.today().isoformat()
    logger.info(f"[Tool] Current date: {today}")
    return today

# ----------------------------
# Agent Setup
# ----------------------------

system_prompt = """
You are an intelligent Task Planning Assistant.
When given a goal, break it into actionable steps, assign realistic deadlines, and prioritize them.
Use get_current_date() tool whenever you need the current date for deadline calculations.
Return results in format:
Task | Deadline | Priority
"""

# Create the LLM (Google Gemini via langchain-google-genai)
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Create the agent (model + tools + system_prompt)
agent = create_agent(
    model=llm,
    tools=[get_current_date],
    system_prompt=system_prompt,
)

# ----------------------------
# Run Example
# ----------------------------
if __name__ == "__main__":
    query = "Plan a 3-day trip to Goa from Pune"
    print("User:", query)

    # Pass conversation as messages with user question
    result = agent.invoke({
        "messages": [
            HumanMessage(content=query)
        ]
    })

    # Print the final content
    print("Agent Response:\n", result["messages"][-1].text)