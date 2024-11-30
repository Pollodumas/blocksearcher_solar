from crewai import Agent
from langchain_community.llms import HuggingFaceHub
from src.tools.analysis_tools import AnalysisTools

class BlockchainAnalyst:
    @staticmethod
    def create(llm: HuggingFaceHub) -> Agent:
        return Agent(
            role='Blockchain Analyst',
            goal='Analyze blockchain research and provide technical insights',
            backstory="""You are a skilled blockchain analyst with expertise in technical analysis 
            and market impact assessment.""",
            tools=[AnalysisTools.content_analyzer()],
            allow_delegation=False,
            llm=llm,
            verbose=True
        )