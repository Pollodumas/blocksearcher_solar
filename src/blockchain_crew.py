from crewai import Crew, Task
from langchain_community.llms import HuggingFaceHub
from typing import Dict, Any
from researcher import BlockchainResearcher
from analyst import BlockchainAnalyst
from report_writer import ReportWriter

class BlockchainResearchCrew:
    def __init__(self, llm: HuggingFaceHub):
        self.researcher = BlockchainResearcher.create(llm)
        self.analyst = BlockchainAnalyst.create(llm)
        self.report_writer = ReportWriter.create(llm)

    def analyze_url(self, url: str) -> Dict[str, Any]:
        research_task = Task(
            description=f"Research and analyze the content at {url}",
            agent=self.researcher
        )

        analysis_task = Task(
            description="Analyze the research findings and provide technical insights",
            agent=self.analyst
        )

        report_task = Task(
            description="Create a comprehensive markdown report from the analysis",
            agent=self.report_writer
        )

        crew = Crew(
            agents=[self.researcher, self.analyst, self.report_writer],
            tasks=[research_task, analysis_task, report_task],
            verbose=True
        )

        return crew.kickoff()