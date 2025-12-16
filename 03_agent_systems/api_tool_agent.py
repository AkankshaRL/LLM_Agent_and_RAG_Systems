# currency_agent.py

import requests
from dotenv import load_dotenv
import logging
from typing import TypedDict
from langchain.tools import tool
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --------------------------------------
# Tools
# --------------------------------------

@tool
def get_currency_factor(base_currency: str, target_currency: str) -> float:
    """
    Fetches the currency conversion rate between base_currency and target_currency.
    """
    logger.info(f"Fetching conversion rate {base_currency} → {target_currency}")
    url = f"https://v6.exchangerate-api.com/v6/aaab0cbba5ec62c0a58ff979/pair/{base_currency}/{target_currency}"
    resp = requests.get(url).json()
    # The API returns the rate under "conversion_rate"
    rate = resp.get("conversion_rate")
    logger.info(f"Rate: {rate}")
    return rate

@tool
def currency_converter(amount: float, conversion_rate: float) -> float:
    """
    Given a conversion rate, returns converted amount.
    """
    result = amount * conversion_rate
    logger.info(f"Converted: {amount} * {conversion_rate} = {result}")
    return result

# --------------------------------------
# Agent Setup
# --------------------------------------

system_prompt = """
You are a helpful assistant that uses tools.
When asked to convert currency, follow these steps:
1. Use get_currency_factor to fetch the latest conversion rate.
2. Use currency_converter to compute the converted amount.
Finally, respond with both the rate and the converted value in a clear format.
"""

# Initialize Gemini (via Google GenAI integration)
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Create the agent
agent = create_agent(
    model=llm,
    tools=[get_currency_factor, currency_converter],
    system_prompt=system_prompt,
)

# --------------------------------------
# Run Example
# --------------------------------------

if __name__ == "__main__":
    prompt = "Convert 20 USD to EUR and show the rate used"
    print("User:", prompt)

    result = agent.invoke({
        "messages": [
            HumanMessage(content=prompt)
        ]
    })

    # The final content is usually in the last message
    output = result["messages"][-1].content
    print("\nAgent Response:")
    print(output)