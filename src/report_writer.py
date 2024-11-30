from crewai import Agent
from langchain_community.llms import HuggingFaceHub
from typing import List

class ReportWriter:
    @staticmethod
    def create(llm: HuggingFaceHub) -> Agent:
        tools: List = []
        return Agent(
            role='Report Writer',
            goal='Create comprehensive blockchain research reports',
            backstory="You are an experienced technical writer specializing in blockchain technology.",
            tools=tools,
            allow_delegation=False,
            llm=llm,
            verbose=True
        )