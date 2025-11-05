import os
from google.adk.agents import Agent
from dotenv import load_dotenv
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent ## => New Added

load_dotenv()
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")

## => New Added. Defines the remote agent server.
remote_country_agent = RemoteA2aAgent(
    name="country_agent",
    agent_card=(
        f"http://localhost:3002" ## => AgentGateway URL for A2A server
    ),
)

travel_agent = Agent(
    name="travel_agent",
    model="gemini-2.0-flash",
    description=(
        "A smart travel assistant that connects users with specialized sub-agents..."
    ),
    instruction=("""
        You are a travel assistant. When a user’s request relates to flights, bookings, visas, or country-specific information, delegate the conversation to the appropriate sub-agent:
        ...
        country_agent for local information, culture, and travel tips
        """),
    sub_agents=[remote_country_agent] ## => New Added
)

root_agent=travel_agent
