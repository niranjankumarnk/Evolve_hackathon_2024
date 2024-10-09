import os
from langchain_community.tools import WikipediaQueryRun, YouTubeSearchTool
from langchain_community.utilities import WikipediaAPIWrapper, ArxivAPIWrapper
from langchain_community.utilities.google_scholar import GoogleScholarAPIWrapper
from langchain_community.tools.google_scholar import GoogleScholarQueryRun
from langchain_community.vectorstores import FAISS
from langchain.tools.retriever import create_retriever_tool
from langchain_core.pydantic_v1 import BaseModel, Field

# Wikipedia Tool
class WikiInputs(BaseModel):
    query: str = Field(description="Query to look up in Wikipedia, should be 3 or fewer words")

def initialize_wikipedia_tool():
    """Initialize Wikipedia tool."""
    api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=500)
    return WikipediaQueryRun(
        name="wiki-tool",
        description="Look up things in Wikipedia",
        args_schema=WikiInputs,
        api_wrapper=api_wrapper,
        return_direct=True,
    )

# YouTube Tool
def initialize_youtube_tool():
    """Initialize YouTube tool."""
    return YouTubeSearchTool()

# Arxiv Tool
def initialize_arxiv_tool():
    """Initialize Arxiv tool."""
    return ArxivAPIWrapper()

# Google Scholar Tool
def initialize_google_scholar_tool():
    """Initialize Google Scholar tool."""
    os.environ["SERP_API_KEY"] = "f39f64a7fef852a21486840761f31b9288a3f24c4e0689c40c16bff722daf5fb"  

# Custom Retriever Tool
def initialize_retriever_tool(db):
    """Initialize custom dataset retriever tool."""
    retriever = db.as_retriever()
    return create_retriever_tool(retriever, 'Mental Health', "Search for information about mental health from the custom dataset")

# Initialize all tools
def initialize_all_tools(db):
    """Initialize all tools."""
    wikipedia_tool = initialize_wikipedia_tool()
    youtube_tool = initialize_youtube_tool()
    arxiv_tool = initialize_arxiv_tool()
    google_scholar_tool = initialize_google_scholar_tool()
    retrieval_tool = initialize_retriever_tool(db)

    return {
        "wikipedia": wikipedia_tool,
        "youtube": youtube_tool,
        "arxiv": arxiv_tool,
        "google_scholar": google_scholar_tool,
        "retrieval": retrieval_tool,
    }
