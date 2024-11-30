from crewai import Agent
from langchain_community.llms import HuggingFaceHub

class ReportWriter:
    @staticmethod
    def create(llm: HuggingFaceHub) -> Agent:
        return Agent(
            role='Report Writer',
            goal='Create comprehensive blockchain research reports',
            backstory="""You are an experienced technical writer specializing in blockchain technology.""",
            tools=[],
            allow_delegation=False,
            llm=llm,
            verbose=True
        )