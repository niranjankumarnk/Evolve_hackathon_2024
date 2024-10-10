# Evolve_hackathon_2024
This is AI Impact Hackathon conducted by Cloudera

# Mental Health Support Assistant
## Used Cloudera Machine Learning Platform and AMP

- Utilized the **Cloudera Machine Learning platform** along with **AMP (Applied Machine Learning Prototype)** for the mental health support assistant project.
- Integrated the platform to streamline project deployment and manage the application environment.

This AMP was built using the [CML Community AMP Template.](https://github.com/cloudera/CML_Community_AMP_Template)
  
## Project Overview
- **Flask-based web application** that serves as a mental health support assistant.
- **Data Sources**: 
  - A Kaggle mental health dataset that has been preprocessed, chunked, tokenized, and stored in a Faiss vector database for efficient retrieval.
  - External sources like **Wikipedia**, **YouTube**, and **Arxiv** are integrated via **LangChain tools** to enrich responses with research papers and videos (e.g., exercises and solutions).

## Components
1. **Data Ingestion**:
   - **Kaggle Mental Health Dataset**: Downloaded, preprocessed, and tokenized into smaller chunks.
   - **Vector Storage with Faiss**: The chunked data is stored in a **Faiss vector database**, allowing efficient retrieval when queries are made.

2. **Retrieval-Augmented Generation (RAG)**:
   - The RAG model is used to retrieve relevant information based on user queries from the vector database, providing personalized responses for mental health queries.
   
3. **LangChain Tools**:
   - **Wikipedia**: Retrieves knowledge-based answers to supplement responses from Faiss.
   - **YouTube**: Provides links to relevant videos like exercises for stress management or relaxation techniques.
   - **Arxiv**: Retrieves academic papers for users interested in more technical or research-based solutions.

## Features
- **Mental Health Support**: Answers user queries about mental health based on stored information and external resources.
- **Exercise Recommendations**: Provides YouTube video links for exercises that help manage anxiety, depression, or stress.
- **Research Papers**: Retrieves related academic papers from Arxiv for users who want deeper knowledge.
- **General Knowledge Support**: Wikipedia integration for factual, generalized queries.

## Next Steps/Improvements
- **Real-Time Data Retrieval**: Ensure that the external sources like Arxiv and YouTube return the most current information.
- **User Feedback Loop**: Implement feedback from users to refine the results further.
- **Expand Dataset**: Add more mental health datasets for increased coverage.
- **Fine-tune Cohere Model**: Continue refining the language model to improve its emotional support capabilities.


## What Was Done Today

### Download Data 
- **Kaggle link**: [Reddit Mental Health Dataset](https://www.kaggle.com/datasets/entenam/reddit-mental-health-dataset)
  - Downloaded data from Kaggle using the `kagglehub` library.

### To Use:

1. **Install `kagglehub`**:
   ```bash
   pip install kagglehub
   
Generate and store Kaggle token:

2. **Go to your Kaggle account and generate an API token.**
   
- This will download a kaggle.json file that contains your credentials.
- Store the kaggle.json file in a .kaggle directory within your home directory:

``` bash
mkdir ~/.kaggle
mv ~/Downloads/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
```

### 1. **Project Structure Setup**

- **Created a structured directory** following AMP (Applied Machine Learning Prototype) guidelines for deployment in Cloudera.
- Set up two main folders for sessions and the application:
  - `0_session-install-dependencies/`: Contains the `install-dependencies.py` script for installing project dependencies.
  - `1_app-run-web-server/`: Contains `app.py` (Flask application) and `index.html` (the template file for the UI).

### 2. **Implemented Flask Application**

- Developed the **Flask web server** (`app.py`) that:
  - Processes user queries using LangChain and Cohere LLM.
  - Fetches responses from various tools (Wikipedia, YouTube, Arxiv).
  - Displays the results on a simple web page.

- **HTML Front-End** (`index.html`):
  - Created a minimal user interface to allow users to submit their queries.
  - Added a form where users can input questions, which will be processed by the backend.

### 3. **Environment and Dependency Setup**

- Added a **`requirements.txt`** file listing all necessary Python packages such as:
  - Flask
  - Cohere
  - LangChain
  - LangChain-Cohere
  - LangChain-Community

- Created **`install-dependencies.py`** in the `0_session-install-dependencies/` folder to automatically install dependencies using `pip`.

### 4. **AMP Metadata Configuration**

- Set up the **`.project-metadata.yaml`** file:
  - Defined environment variables, including `COHERE_API_KEY` for secure access to the Cohere API.
  - Set the tasks for installing dependencies and running the Flask web server.

### 5. **Tested and Debugged AMP Setup**

- Successfully tested the AMP deployment using Cloudera Machine Learning (CML) environment.
- Verified that both installation and web application tasks ran without errors.
- Made sure the web app was accessible on the assigned `CDSW_APP_PORT`.

## How to Use

### Prerequisites

- Python 3.10 or higher
- Set the `COHERE_API_KEY` environment variable.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/mental-health-assistant-amp.git
