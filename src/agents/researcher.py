from crewai import Agent
from langchain_community.llms import HuggingFaceHub
from src.tools.search_tools import SearchTools

class BlockchainResearcher:
    @staticmethod
    def create(llm: HuggingFaceHub) -> Agent:
        return Agent(
            role='Blockchain Researcher',
            goal='Research and analyze blockchain content',
            backstory="""You are an expert blockchain researcher with extensive experience in analyzing 
            blockchain technologies, market trends, and technical implementations.""",
            tools=[SearchTools.web_search()],
            allow_delegation=False,
            llm=llm,
            verbose=True
        )