# AI-Powered Contract Intelligence Platform
An advanced, automated legal document analysis system designed to parse standard PDF contracts, extract core entities, evaluate regulatory compliance flags, and enable high-speed semantic search over localized clause databases
##  About the Project & Work Don
Manual review of legal documents is traditionally time-consuming, expensive, and prone to human oversight. This project introduces an **AI-Powered Contract Intelligence Platform** to fully automate the parsing and risk-assessment pipeline. 
By leveraging cutting-edge Natural Language Processing (NLP) pipelines and Deep Learning models, the system ingests raw PDF contracts, extracts critical operational entities, classifies hidden compliance risks, and indexes clauses into a localized vector database for instant semantic search capability.
### Core Architecture Modules:
1. **Extraction Engine (spaCy)**: Parses raw, unstructured text to capture foundational variables like corporate identities, operational dates, and monetary values.
2. **Zero-Shot Risk Classification (BART Large MNLI)**: Employs a deep learning model to evaluate legal clauses against compliance risks (e.g., liability limits, data leaks) without requiring a pre-labeled training dataset.
3. **Vector Storage & Semantic Exploration (ChromaDB)**: Embeds and indexes sentences into a specialized vector store, allowing users to scan for hidden liabilities using conceptual terms instead of basic keyword matching.
##  System Stack

The application is engineered using high-performance web and data-science frameworks:
* **Backend Framework**: FastAPI (Uvicorn ASGI Server)
* **Natural Language Processing (NLP)**: spaCy (`en_core_web_sm`)
* **Deep Learning Engine**: Hugging Face Transformers (`bart-large-mnli`)
* **Vector Database**: ChromaDB (for structural text-embedding persistence)
* **Frontend Interface**: TailwindCSS + Vanilla JavaScript Dashboard
##  Project Directory Structure

```text
contract_intelligence/
├── app/                  # Main backend server & FastAPI routing logic
├── data/                 # Local directory for document storage & persistence
├── utils/                # AI inference engines, tokenizers, & processing helper scripts
├── launch.bat            # Automated local orchestration & server startup script
└── requirements.txt      # Core Python library dependencies

 Setup & How to Run the Project
1. Prerequisites
Ensure you have Python 3.10+ installed on your Windows environment.

2. Environment Initialization
Before launching the script, open your terminal in the root directory and install the necessary dependencies:

Bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
3. Launching the Application Server
To boot up the complete AI pipeline and local server:

Open your project folder (C:\Users\Pranathi\contract_intelligence).

Double-click the launch.bat file.

A black Command Prompt window will appear. Wait approximately 30 to 60 seconds for the heavy AI models to load into memory.

Once you see the line INFO: Application startup complete., the server is active.

4. Accessing the Dashboard
Open your web browser and go to: http://127.0.0.1:8000

Tip: You can safely Minimize (—) the black terminal window to clear your desktop, but do not close it (clicking X will shut down the server engine).
