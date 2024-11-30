from crewai import Agent
from langchain_community.llms import HuggingFaceHub
from langchain_core.tools import Tool
from typing import List

class BlockchainAnalyst:
    @staticmethod
    def create(llm: HuggingFaceHub) -> Agent:
        tools: List = [
            Tool(
                name="content_analyzer",
                description="Analyze blockchain content and provide insights",
                func=lambda x: {"analysis": x}
            )
        ]
        return Agent(
            role='Blockchain Analyst',
            goal='Analyze blockchain research and provide technical insights',
            backstory="You are a skilled blockchain analyst with expertise in technical analysis.",
            tools=tools,
            allow_delegation=False,
            llm=llm,
            verbose=True
        )