import os
from dotenv import load_dotenv
from google.adk.agents import Agent
# from .instructions import country_agent_instruction, exchange_agent_instruction
# from google.adk.tools.mcp_tool import MCPToolset, StreamableHTTPConnectionParams
# from .tools import get_country_info,get_public_holidays,get_weather_forecast,get_current_date ,get_exchange_rate
# from google.adk.a2a.utils.agent_to_a2a import to_a2a ## => New Added
load_dotenv()
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")



# tool_set=MCPToolset(
#     connection_params=StreamableHTTPConnectionParams(
#         url="http://localhost:8001/mcp" ## => Our MCP Server
#     ),
# )


# country_agent_tool_set=MCPToolset(
#    connection_params=StreamableHTTPConnectionParams(
#        url="http://localhost:3000",
#    ),
#    #tool_filter=["get_country_info","get_public_holidays","get_weather_forecast","get_current_date"]
# )

# exchange_agent_tool_set=MCPToolset(
#    connection_params=StreamableHTTPConnectionParams(
#        url="http://localhost:3001"
#    ),
#    #tool_filter=["get_current_date" ,"get_exchange_rate"]
# )



# exchange_agent=Agent(
#    name="exchange_agent",
#    model="gemini-2.0-flash",
#    description=(
#        "An agent that gives information about the exchange rates"
#    ),
#    instruction=exchange_agent_instruction,
#    tools=[exchange_agent_tool_set]
# )

country_agent = Agent(
   name="country_agent",
   model="gemini-2.0-flash",
   # description="An agent that provides information about the country",
   # instruction=country_agent_instruction,
   # tools=[country_agent_tool_set],
   # sub_agents=[exchange_agent]
)

root_agent=country_agent

# country_agent_server=to_a2a(root_agent)