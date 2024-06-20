from crewai import Task
from tools import search_tool,PDFSearchTool
from agents import blood_report_analyst, researcher

## Research Task
report_analyze_task = Task(
  description=(
    "Analyze the {blood_report}."
    "Summarize it in an easy to understand manner"
  ),
  expected_output='A comprehensive summary based on the {blood_report} covering all the important aspects of the blood report analysis.',
  tools = [PDFSearchTool],
  agent=blood_report_analyst,
  model = 'gpt-4o'
)

# Writing task with language model configuration
research_task = Task(
  description=(
    "search the web based on the summary of the {blood_report} and give health recommendations also provide links to the relevant articles."
  ),
  expected_output='Give health recommendations for the {blood_report} based on its analysis in points and provide relevant links for the articles.',
  agent=researcher,
  async_execution=False,
  tools=[PDFSearchTool, search_tool],
  model = 'gpt-4o',
  output_file='readable-blood-report.md'  # Example of output customization
)