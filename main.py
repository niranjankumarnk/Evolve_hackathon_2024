from flask import Flask, render_template, request
import os
from preprocess import load_data, split_text_into_chunks, generate_embeddings_and_store_faiss
from tools import initialize_all_tools
from langchain_community.llms import Cohere
from langchain.agents import create_react_agent
from langchain_community.embeddings import HuggingFaceEmbeddings

app = Flask(__name__)
# Set Cohere API key in environment
os.environ["COHERE_API_KEY"] = "996fB69PNLQjAiH4N2fnmTl4ccii91iz2Xr4mTfE"  

# Function to initialize the model and tools
def initialize_model_and_tools():
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

    # Initialize agent with tools and LLM using create_react_agent
    agent = create_react_agent(
        tools=tool_list,
        llm=llm,
    )

    return agent, tools

# Cache the initialized agent and tools
agent, tools = initialize_model_and_tools()

# Function to format response
def format_response(wiki_data, pubmed_data, arxiv_data, youtube_data, retrieval_data):
    response = "<h2>Solutions for Overcoming Depression</h2>"
    if retrieval_data:
        response += f"<h3>Retrieved from database:</h3><p>{retrieval_data}</p>"
    if wiki_data:
        response += f"<h3>General Information (Wikipedia):</h3><p>{wiki_data}</p>"
    if arxiv_data:
        response += f"<h3>Research Papers (Arxiv):</h3><p>{arxiv_data}</p>"
    if youtube_data:
        response += f"<h3>Exercise Videos (YouTube):</h3><p>{youtube_data}</p>"
    return response

@app.route('/', methods=['GET', 'POST'])
def index():
    formatted_response = ""
    if request.method == 'POST':
        # Get user input query from form
        query = request.form.get('query', '')

        # Run the query through the tools and agent
        retrieval_data = tools['retrieval'].run(query)
        wiki_data = tools['wikipedia'].run(query)
        pubmed_data = "PubMed data not integrated in this example"  # Placeholder for PubMed
        arxiv_data = tools['arxiv'].run(query)
        youtube_data = tools['youtube'].run(query)

        # Format the response
        formatted_response = format_response(wiki_data, pubmed_data, arxiv_data, youtube_data, retrieval_data)

    return render_template('index.html', response=formatted_response)

if __name__ == '__main__':
    app.run(debug=True)




