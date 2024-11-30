import streamlit as st
from langchain_community.llms import HuggingFaceHub
from blockchain_crew import BlockchainResearchCrew
from config import init_page
from report import display_results

def main():
    init_page()
    
    # Initialize LLM and Crew
    llm = HuggingFaceHub(
        repo_id="upstage/SOLAR-10.7B-Instruct-v1.0",
        huggingfacehub_api_token=st.secrets["HUGGINGFACEHUB_API_TOKEN"],
        model_kwargs={
            "max_new_tokens": 4096,
            "temperature": 0.2,
            "top_p": 0.95,
            "do_sample": True
        }
    )
    # Override the API URL to use the specific model endpoint
    llm.client.api_url = "https://api-inference.huggingface.co/models/upstage/SOLAR-10.7B-Instruct-v1.0"
    
    crew = BlockchainResearchCrew(llm)

    # User interface
    with st.form("research_form"):
        url = st.text_input(
            "URL to analyze:",
            placeholder="Enter the URL of blockchain article or resource"
        )
        submitted = st.form_submit_button("Start Analysis")

    if submitted and url:
        if not url.startswith(('http://', 'https://')):
            st.error("Please enter a valid URL starting with http:// or https://")
            return

        with st.spinner("🤖 AI Crew analyzing content..."):
            try:
                result = crew.analyze_url(url)
                display_results(result)
            except Exception as e:
                st.error(f"Error during analysis: {str(e)}")
                st.error("Please try again with a different URL or contact support if the issue persists.")

if __name__ == "__main__":
    main()