import asyncio
from acp_sdk import Message, MessagePart, GenericEvent
from acp_sdk.server import Context, Server
from crewai import Agent, Task, Crew
import json
from dotenv import load_dotenv
from crewai.llm import LLM

load_dotenv()

llm = LLM(model = "gemini-2.5-flash")

# Mock data
MOCK_FLIGHTS = {"Paris": {"date": "2025-06-06", "time": "10:00 AM", "flight": "AF123", "price": 300}}
MOCK_HOTELS = {"Paris": {"check_in": "2025-06-06", "nights": 2, "hotel": "Hotel Paris", "price": 200}}
MOCK_WEATHER = {"Paris": {"date": "2025-06-06", "forecast": "Sunny, 75°F"}}

server = Server()

@server.agent("trip_planning_coordinator")
async def trip_planning_coordinator(input: list[Message], context: Context):
    """Coordinates trip planning for Paris using ACP protocol"""
    user_request = input[-1].parts[0].content
    yield MessagePart(content=f"Processing request: {user_request}\n")

    # Define Agents
    client_agent = Agent(
        role="Client Agent",
        goal="Coordinate trip planning for Paris using ACP protocol",
        backstory="A helpful assistant that delegates tasks via ACP.",
        verbose=True,
        llm=llm
    )
    flight_agent = Agent(role="Flight Agent", goal="Find flights via ACP", backstory="Flight schedule expert.", verbose=True, llm=llm)
    hotel_agent = Agent(role="Hotel Agent", goal="Book hotels via ACP", backstory="Hotel reservation specialist.", verbose=True, llm=llm)
    weather_agent = Agent(role="Weather Agent", goal="Provide weather forecast via ACP", backstory="Meteorology expert.", verbose=True, llm =llm)

    # Mock capabilities
    capabilities = {
        "flight_agent": ["find_flight", "book_flight"],
        "hotel_agent": ["find_hotel", "book_hotel"],
        "weather_agent": ["get_forecast"]
    }

    # Client task logic
    async def client_task_func():
        flight_capable = "find_flight" in capabilities["flight_agent"]
        hotel_capable = "find_hotel" in capabilities["hotel_agent"]
        weather_capable = "get_forecast" in capabilities["weather_agent"]

        if flight_capable:
            yield MessagePart(content="Requesting flight details...\n")
            flight_response = MOCK_FLIGHTS["Paris"]
        if hotel_capable and flight_response:
            yield MessagePart(content="Requesting hotel booking...\n")
            hotel_response = MOCK_HOTELS["Paris"]
        if weather_capable:
            yield MessagePart(content="Requesting weather forecast...\n")
            weather_response = MOCK_WEATHER["Paris"]
        
        plan = (f"Trip Plan for Paris:\n"
                f"- Flight booked: {flight_response['flight']} on {flight_response['date']} at {flight_response['time']}, ${flight_response['price']}\n"
                f"- Hotel booked: {hotel_response['hotel']} on {hotel_response['check_in']} for {hotel_response['nights']} nights, ${hotel_response['price']}, check-in ready after flight at {flight_response['time']}\n"
                f"- Weather forecast: {weather_response['date']}, {weather_response['forecast']}")
        yield MessagePart(content=plan)

    client_task = Task(
        description="Coordinate trip to Paris using ACP protocol.",
        agent=client_agent,
        async_execution=True,
        expected_output="A coordinated trip plan for Paris.",
        function=client_task_func
    )
    flight_task = Task(description="Find a flight to Paris.", agent=flight_agent, async_execution=False, expected_output="Flight details.")
    hotel_task = Task(description="Book a hotel in Paris.", agent=hotel_agent, async_execution=False, expected_output="Hotel details.")
    weather_task = Task(description="Get weather forecast for Paris.", agent=weather_agent, async_execution=False, expected_output="Weather forecast.")

    crew = Crew(
        agents=[client_agent, flight_agent, hotel_agent, weather_agent],
        tasks=[client_task, flight_task, hotel_task, weather_task],
        verbose=True,
    )

    yield MessagePart(content="Starting trip planning with ACP crew...\n")
    
    try:
        result = await crew.kickoff_async()
        yield MessagePart(content=result.raw)
    except Exception as e:
        yield MessagePart(content=f"Error during planning: {str(e)}")

if __name__ == "__main__":
    server.run()