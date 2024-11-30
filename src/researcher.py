from crewai import Agent
from langchain_community.llms import HuggingFaceHub
from langchain_community.tools import DuckDuckGoSearchRun
from typing import List

class BlockchainResearcher:
    @staticmethod
    def create(llm: HuggingFaceHub) -> Agent:
        tools: List = [DuckDuckGoSearchRun()]
        return Agent(
            role='Blockchain Researcher',
            goal='Research and analyze blockchain content',
            backstory="You are an expert blockchain researcher with extensive experience in analyzing blockchain technologies.",
            tools=tools,
            allow_delegation=False,
            llm=llm,
            verbose=True
        )