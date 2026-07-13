# AI Contract Intelligence System

## Project Overview
The AI Contract Intelligence System is an enterprise-grade document intelligence platform designed to ingest unstructured legal contracts, perform high-precision Named Entity Recognition (NER), build semantic vector indexes, and run deep contextual transformer inferences to classify clause vulnerabilities.
## 🎖️ Module Ownership & Architecture Breakdowns

### 👤 Gandikota Prasannatha (Lead AI & Data Infrastructure Engineer)
I engineered and successfully compiled the entire production-ready AI pipeline, local vector database storage layer, and quick-start environment automation scripts. **My working code is fully operational and isolated within the following directories:**

* **📂 `/app` (FastAPI Core Application):**
  * Handled multi-part form data uploads for contract documents.
  * Formulated request/response validation logic and exposed public API integration routes.
* **📂 `/utils` (NLP Engine & Vector DB Store):**
  * *`nlp_engine.py`:* Wired up the `spaCy` Named Entity Recognition pipeline along with the Hugging Face Large-Scale Zero-Shot Transformer model (`bart-large-mnli`) to score structural clause vulnerabilities with high mathematical precision.
  * *`vector_store.py`:* Built the system text chunking logic and integrated localized `ChromaDB` storage to index high-dimensional semantic vector embeddings.
* **📄 `launch.bat`:** Created the automated environment script for one-click runtime setups without manual shell navigation.

## 📅 Implementation Roadmap

### Week 1 & 2 Core Fundamentals
* **FastAPI Backend Development:** Multi-part file stream management.
* **PDF Upload & Processing:** Binary ingestion handling via `pypdf`.
* **Named Entity Recognition (NER):** Automatic extraction of **Organizations (`ORG`)**, **Dates (`DATE`)**, and **Currency (`MONEY`)** using pre-trained pipelines.
* **Vector Vector Store:** Local persistence layer and high-dimensional semantic search indexing inside `ChromaDB`.
* **Deep Text Clause Inference:** Sentence-level contextual checks running on local CPU resources.

### Processing Pipeline Flow
