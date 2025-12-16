import asyncio
import platform
from crewai import Agent, Task, Crew
from crewai.llm import LLM
import json
from dotenv import load_dotenv

load_dotenv()

# Mock data
MOCK_FLIGHTS = {"Paris": {"date": "2025-06-06", "time": "10:00 AM", "flight": "AF123", "price": 300}}
MOCK_HOTELS = {"Paris": {"check_in": "2025-06-06", "nights": 2, "hotel": "Hotel Paris", "price": 200}}
MOCK_WEATHER = {"Paris": {"date": "2025-06-06", "forecast": "Sunny, 75°F"}}

llm = LLM(model = "gemini-2.5-flash")
# A2A Agent Card
def create_agent_card(agent_name, capabilities, endpoint):
    return {
        "agent_name": agent_name,
        "capabilities": capabilities,
        "endpoint": endpoint,
        "authentication": {"scheme": "Bearer", "token": f"mock-token-{agent_name}"}
    }

# A2A message (JSON-RPC 2.0)
def create_a2a_message(sender, receiver, method, params, task_id):
    return {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": task_id,
        "role": "agent",
        "sender": sender,
        "receiver": receiver
    }

# Define Agents
client_agent = Agent(
    role="Client Agent",
    goal="Coordinate trip planning for Paris using A2A protocol",
    backstory="A helpful assistant that delegates tasks via A2A.",
    verbose=True,
    llm = llm
)
flight_agent = Agent(role="Flight Agent", goal="Find flights via A2A", backstory="Flight schedule expert.", verbose=True, llm = llm)
hotel_agent = Agent(role="Hotel Agent", goal="Book hotels via A2A", backstory="Hotel reservation specialist.", verbose=True, llm = llm)
weather_agent = Agent(role="Weather Agent", goal="Provide weather forecast via A2A", backstory="Meteorology expert.", verbose=True, llm = llm)

# A2A Agent Cards
agent_cards = {
    "flight_agent": create_agent_card("flight_agent", ["find_flight", "book_flight"], "/flight_endpoint"),
    "hotel_agent": create_agent_card("hotel_agent", ["find_hotel", "book_hotel"], "/hotel_endpoint"),
    "weather_agent": create_agent_card("weather_agent", ["get_forecast"], "/weather_endpoint")
}

# Client Task
async def client_task_func():
    task_id = "task-001"
    flight_capable = "find_flight" in agent_cards["flight_agent"]["capabilities"]
    hotel_capable = "find_hotel" in agent_cards["hotel_agent"]["capabilities"]
    weather_capable = "get_forecast" in agent_cards["weather_agent"]["capabilities"]
    
    if flight_capable:
        flight_msg = create_a2a_message("client_agent", "flight_agent", "find_flight", 
                                        {"destination": "Paris", "date": "2025-06-06"}, task_id)
        flight_response = MOCK_FLIGHTS["Paris"]
    if hotel_capable and flight_response:
        hotel_msg = create_a2a_message("client_agent", "hotel_agent", "book_hotel", 
                                       {"destination": "Paris", "check_in": "2025-06-06", "nights": 2, 
                                        "flight_arrival": flight_response["time"]}, task_id)
        hotel_response = MOCK_HOTELS["Paris"]
    if weather_capable:
        weather_msg = create_a2a_message("client_agent", "weather_agent", "get_forecast", 
                                         {"destination": "Paris", "date": "2025-06-06"}, task_id)
        weather_response = MOCK_WEATHER["Paris"]
    
    plan = (f"Trip Plan for Paris:\n"
            f"- Flight booked: {flight_response['flight']} on {flight_response['date']} at {flight_response['time']}, ${flight_response['price']}\n"
            f"- Hotel booked: {hotel_response['hotel']} on {hotel_response['check_in']} for {hotel_response['nights']} nights, ${hotel_response['price']}, check-in ready after flight at {flight_response['time']}\n"
            f"- Weather forecast: {weather_response['date']}, {weather_response['forecast']}")
    return plan

client_task = Task(
    description="Coordinate trip to Paris using A2A protocol.",
    agent=client_agent,
    async_execution=True,
    expected_output="A coordinated trip plan for Paris.",
    function=client_task_func
)
flight_task = Task(description="Find a flight to Paris.", agent=flight_agent, async_execution=False, expected_output="Flight details.")
hotel_task = Task(description="Book a hotel in Paris.", agent=hotel_agent, async_execution=False, expected_output="Hotel details.")
weather_task = Task(description="Get weather forecast for Paris.", agent=weather_agent, async_execution=False, expected_output="Weather forecast.")

# Create Crew
crew = Crew(
    agents=[client_agent, flight_agent, hotel_agent, weather_agent],
    tasks=[client_task, flight_task, hotel_task, weather_task],
    verbose=True,
    tracing = True
)

# Main execution
async def main():
    print("=== Trip Planning with A2A Protocol ===")
    print("Agent Cards for Discovery:")
    print(json.dumps(agent_cards, indent=2))
    print("\nRunning trip planning...")
    result = await crew.kickoff_async()
    print("\nFinal Trip Plan:")
    print(result)

if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main())