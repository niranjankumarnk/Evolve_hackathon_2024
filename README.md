# Evolve_hackathon_2024
This is AI Impact Hackathon conducted by Cloudera

![Won 3rd place]("C:\Users\Niranjan kumar\Downloads\evolve_hackathon_3rd place.jpeg")

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
mv ~/path/to/kaggle.json ~/.kaggle/
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
  - Cohere (LLM)
  - LangChain
  - LangChain-Cohere
  - LangChain-Community
  - Sentence-transformers (Embeddings)

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


## Result produced during experiment:( Check in Experiment.ipynb)

### Query :  "How to overcome anxiety and give some tips and exercise video "

## Solutions for Overcoming Anxiety

### Retrieved from Database:

selftext: I have started a new sales job a few months ago. And has started triggering my anxiety pretty bad. I exercise and run most days of the week and it is still not helping enough. I have been meditating too and does not seem to help yet either. I have noticed after meditating I am more prone to feel my anxiety physical sensation with tension in head and stomach. It is best to accept these sensations and just keep on meditating. Or is it better to just try to make my self feel courage when I experience anxiety and these feelings? Advice is much appreciated
subreddit: Anxiety
title: Need Help With Best Way to Deal with My Anxiety
Label: Trauma and Stress

Has anyone figured out a way to balance not going in about every little thing and making sure you’re being respected and heard?

Also, what are some things y’all do to ground yourself during an anxiety or panic attack? Bc the techniques I have ain’t doing a gd thing lbvs
subreddit: Anxiety
title: Anxiety Tonight
Label: Personality

That progressed into figuring out how to use it in small doses to control the anxiety in any social environment.  I know how to control my anxiety I know the exact things I need to do what to tell myself when it happens who to call to calm me down.  And the easiest and fastest way.  Alcohol.I appear on the outside like I know what’s going on with me.  I can present myself as a normal human most of the time.  However this is not healthy.  I’m in a place where now I don’t want to engage in these things to “cure” myself . I’m trying hard to focus on what will actually fix me now and that’s why I don’t appear to be falling apart but I am.  Deeply I want to change and I want to be healthy.  I want to be able to care for myself.  So that I can actually function.  Imagine how much better of a person I can become if I don’t have this anxiety hanging over my head.

i’m really scared that something will happen to me, or that i’m going crazy. 

i also had a panic attack while high, but i was completely fine until suddenly everything hit, and boom daily panic attacks. 
how can i distract myself and take back my life? there’s no big sources like therapy or that much counseling where i live and this is the only place i can think of where people can potions understand what i’m going through
subreddit: Anxiety
title: does anyone else have this big fear of suddenly losing control of reality?
Label: Drug and Alcohol



### General Information:

Page: Eating disorder
Summary: An eating disorder is a mental disorder defined by abnormal eating behaviors that adversely affect a person's physical or mental health. These behaviors include eating either too much or too little. Types of eating disorders include binge eating disorder, where the patient keeps eating large amounts in a short period of time typically while not being hungry; anorexia nervosa, where the person has an intense fear of gaining weight and restricts food or overexercises

### Research Papers:
Published: 2023-11-09
Title: Exploring and Analyzing the Effect of Avatar's Realism on Anxiety of English as Second Language (ESL) Speakers
Authors: Tianqi Liu, Joshua Rafael Sanchez, Yuntao Wang, Xin Yi, Yuanchun Shi
Summary: The emergence of virtual avatars provides innovative opportunities for remote conferencing, education, and more. Our study investigates how the realism of
avatars, used by native English speakers, impacts the anxiety levels of English as a Second Language (ESL) speakers during interactions. ESL participants
engaged in conversations with native English speakers represented through cartoonish avatars, realistic-like avatars, or actual video streams. We measured both the ESL speakers' self-reported anxiety and their physiological indicators of anxiety. Our findings show that interactions with native speakers using cartoonish avatars or direct video lead to reduced anxiety levels among ESL participants. However, interactions with avatars that closely resemble humans heightened these anxieties. These insights are critically important for the design and application of virtual avatars, especially in addressing cross-cultural communication barriers and enhancing user experience.

Published: 2024-07-08
Title: Bounded confidence modeling predicts how group work affects student math anxiety
Authors: Katherine Toms, Maya Williams, Matthew S. Mizuhara
Summary: Math anxiety is ubiquitous. It not only affects student performance and confidence, but also can lead to avoidance of further math/STEM classes and careers. Cooperative learning (i.e., group work) is a proven strategy that can reduce math anxiety and has additional social and pedagogical benefits. However, depending on the individuals involved, some peer interactions may mitigate anxiety while others exacerbate it. Mathematical modeling is one approach to help untangle this complex dynamic. In this work we introduce a bounded confidence model to evaluate how math anxiety levels are affected by student group work. Although the model is quite simple, it captures non-obvious phenomena including how varying group sizes and frequency of switching groups can affect anxiety levels. The model is easily adaptable to incorporate additional personal and societal factors making it ripe for future research.

Published: 2021-04-20
Title: Development of digitally obtainable 10-year risk scores for depression and anxiety in the general population
Authors: D. Morelli, N. Dolezalova, S. Ponzo, M. Colombo, D. Plans
Summary: The burden of depression and anxiety in the world is rising. Identification of individuals at increased risk of developing these conditions would help to target them for prevention and ultimately reduce the healthcare burden. We developed a 10-year predictive algorithm for depression and anxiety using the full cohort of over 400,000 UK Biobank (UKB) participants without pre-existing depression or anxiety using digitally obtainable information. From the initial 204 variables selected from UKB, processed into > 520 features, iterative backward elimination using Cox proportional hazards model was performed to select predictors which account for the majority of its predictive capability. Baseline and reduced models were then trained for depression and anxiety using both Cox and DeepSurv, a deep neural network approach to survival analysis. The baseline Cox model achieved concordance of 0.813 and 0.778 on the validation dataset for depression and anxiety, respectively. For the DeepSurv model, respective concordance indices were 0.805 and 0.774. After feature selection, the depression model contained 43 predictors and the concordance index was 0.801 for both Cox and DeepSurv. The reduced anxiety model, with 27 predictors, achieved concordance of 0.770 in both models. The final models showed good
discrimination and calibration in the test datasets.We developed predictive risk scores with high discrimination for depression and anxiety using the UKB cohort, incorporati

### Exercise Videos:
- [Video 1: How to overcome anxiety and give some tips and exercise](https://www.youtube.com/watch?v=1XCObQjSHIs)
- [Video 2: Another video on exercises to overcome anxiety](https://www.youtube.com/watch?v=4QHGYTP5HsE)



