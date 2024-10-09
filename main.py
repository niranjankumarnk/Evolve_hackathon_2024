import os
from preprocess import load_data, split_text_into_chunks, generate_embeddings_and_store_faiss
from tools import initialize_all_tools
from langchain.agents import initialize_agent, Tool
from langchain.llms import Cohere

# Set Cohere API key in environment
os.environ["COHERE_API_KEY"] = "996fB69PNLQjAiH4N2fnmTl4ccii91iz2Xr4mTfE"  # Replace with your Cohere API key

def format_response(wiki_data, pubmed_data, arxiv_data, youtube_data, retrieval_data):
    """Format the response from different tools."""
    response = "## Solutions for Overcoming Depression\n\n"
    
    response += f"### Retrieved from database:\n{retrieval_data}\n\n"
    response += f"### General Information (Wikipedia):\n{wiki_data}\n\n"
    response += f"### Research Papers (Arxiv):\n{arxiv_data}\n\n"
    response += f"### Exercise Videos (YouTube):\n{youtube_data}\n\n"
    
    return response

if __name__ == "__main__":
    # Preprocess data (adjust file paths as needed)
    file_path = "processed_data.csv"
    mental_health_data = load_data(file_path)
    chunks = split_text_into_chunks(mental_health_data)
    db, texts = generate_embeddings_and_store_faiss(chunks)

    # Initialize tools
    tools = initialize_all_tools(db)

    # Initialize Cohere LLM
    llm = Cohere(model="command-xlarge-nightly")

    # Wrap tools in LangChain's Tool class
    tool_list = [
        Tool(name="Wikipedia", func=tools['wikipedia'].run, description="Search information from Wikipedia"),
        Tool(name="YouTube", func=tools['youtube'].run, description="Fetch video information from YouTube"),
        Tool(name="Arxiv", func=tools['arxiv'].run, description="Fetch research papers from Arxiv"),
        Tool(name="Vector Retrieval", func=tools['retrieval'].run, description="Retrieve documents from the vector store")
    ]

    # Initialize agent with tools and LLM
    agent = initialize_agent(
        tools=tool_list,
        llm=llm,
        agent_type="zero-shot-react-description",
    )

    # Query and fetch data
    query = "How to overcome anxiety and give some tips and exercise video"
    retrieval_data = tools['retrieval'].run(query)
    wiki_data = tools['wikipedia'].run(query)
    pubmed_data = "PubMed data not integrated in this example"  # Placeholder for PubMed
    arxiv_data = tools['arxiv'].run(query)
    youtube_data = tools['youtube'].run(query)

    # Format the response
    formatted_response = format_response(wiki_data, pubmed_data, arxiv_data, youtube_data, retrieval_data)
    
    # Output the response
    print(formatted_response)


