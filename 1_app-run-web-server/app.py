from flask import Flask, render_template, request
import os
from preprocess import load_data, split_text_into_chunks, generate_embeddings_and_store_faiss
from tools import initialize_all_tools
from langchain_community.llms import Cohere
from langchain.agents import create_react_agent

app = Flask(__name__)

# Check if COHERE_API_KEY is set
if not os.getenv("COHERE_API_KEY"):
    raise EnvironmentError("COHERE_API_KEY is not set. Please set the API key.")

def initialize_model_and_tools():
    file_path = "processed_data.csv"
    mental_health_data = load_data(file_path)
    chunks = split_text_into_chunks(mental_health_data)
    db, texts = generate_embeddings_and_store_faiss(chunks)

    tools = initialize_all_tools(db)
    llm = Cohere(model="command-xlarge-nightly")

    tool_list = [
        Tool(name="Wikipedia", func=tools['wikipedia'].run, description="Search Wikipedia"),
        Tool(name="YouTube", func=tools['youtube'].run, description="Fetch YouTube videos"),
        Tool(name="Arxiv", func=tools['arxiv'].run, description="Fetch Arxiv papers"),
        Tool(name="Vector Retrieval", func=tools['retrieval'].run, description="Retrieve documents from the database")
    ]

    agent = create_react_agent(tools=tool_list, llm=llm)
    return agent, tools

agent, tools = initialize_model_and_tools()

@app.route('/', methods=['GET', 'POST'])
def index():
    response = ""
    if request.method == 'POST':
        query = request.form.get('query', '')
        retrieval_data = tools['retrieval'].run(query)
        wiki_data = tools['wikipedia'].run(query)
        arxiv_data = tools['arxiv'].run(query)
        youtube_data = tools['youtube'].run(query)
        
        response = f"<h3>Results:</h3><p>{retrieval_data}</p><p>{wiki_data}</p><p>{arxiv_data}</p><p>{youtube_data}</p>"

    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv("CDSW_APP_PORT", 5000)))

