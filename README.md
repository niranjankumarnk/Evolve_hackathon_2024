# Evolve_hackathon_2024
This is AI Impact Hackathon conducted by Cloudera

# Mental Health Assistant AMP

This project is a Flask-based web application that leverages Cohere's language model and LangChain to provide mental health assistance by retrieving information from sources such as Wikipedia, YouTube, Arxiv, and a custom database.

## What Was Done Today

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
