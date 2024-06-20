from crewai import Agent
from tools import search_tool, PDFSearchTool
from dotenv import load_dotenv

load_dotenv()

import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4o"
# Create a Blood report analyst
blood_report_analyst = Agent(
    role='Blood report Analyst',
    goal='analyze the {blood_report} and summarize it in an easy to understand manner',
    verbose=True,
    memory=True,
    backstory=(
       "You are an expert in analyzing blood reports and summarizing it in an easy to understand manner" 
    ),
    tools=[PDFSearchTool],
    model = 'gpt-4o',
    allow_delegation=False
)

# Create a Researcher
researcher = Agent(
    role='Researcher',
    goal='Search the web based on the {blood_report}',
    verbose=True,
    memory=True,
    backstory=(
        "You are researcher who is expert in searching the web, you should search the web for articles tailored to the person's health needs based on the blood test results, and"
        "finally, you should give health recommendations and provide links to the relevant articles as well."
    ),
    tools=[PDFSearchTool,search_tool],
    model = 'gpt-4o',
    allow_delegation=False
)