# crewai_integration.py
from crewai import Agent, Task, Crew
from salesforce_tools import SearchLeadTool, CreateLeadTool, GetOpportunityTool
import os
from dotenv import load_dotenv

load_dotenv()

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Create a lead qualification agent
multi_mode_agent = Agent(
    role="Lead Qualification Specialist",
    goal="Analyze prospect information to identify high-intent buyers",
    backstory="Expert in identifying buying signals and qualification criteria in real estate",
    verbose=True,
    tools=[SearchLeadTool(), CreateLeadTool(), GetOpportunityTool()]
)

# Create a lead qualification task
qualify_lead_task = Task(
    description="""
    You need to qualify a potential real estate lead:
    1. Check if the lead already exists in Salesforce by email
    2. If not, create a new lead with the provided information
    3. Analyze the lead information to determine buying intent and potential
    
    Lead information:
    Name: Jane Jenifer
    Email: jane.jenifer@gmail.com
    Phone: 555-123-4568
    Property Interest: Single Family Home
    """,
    expected_output="A detailed lead qualification report including whether the lead was found or created in Salesforce, and an assessment of their buying potential",
    agent=multi_mode_agent
)

# get an opportunity
opportunity_task = Task(
    description="""
    You need to get an opportunity from Salesforce by ID:
    1. Retrieve the opportunity by ID
    2. Return the opportunity information
    3. Ensure the information is not in JSON format and summarized for better understanding
    
    Opportunity ID: 006J400000OAWTCIA5
    """,
    expected_output="The opportunity information in a summarized format",
    agent=multi_mode_agent
)

# Create the crew
real_estate_crew = Crew(
    agents=[multi_mode_agent],
    tasks=[qualify_lead_task, opportunity_task],
    verbose=True
)

# Run the crew
result = real_estate_crew.kickoff()
print("\n=== Crew Result ===")
print(result)
