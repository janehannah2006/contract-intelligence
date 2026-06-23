# AI Contract Intelligence System

## Project Overview

The AI Contract Intelligence System analyzes legal contracts and extracts useful information such as contract type, entities, clauses, and metadata.

## Week 1 Implementation

### Features
- FastAPI Backend Development
- PDF Upload Functionality
- Text Extraction from Contracts
- OCR Support for Scanned Documents
- Named Entity Recognition (NER)
- Clause Detection
- Risk Analysis

## Week 2 - NLP Pipeline Implementation

### Contract Tokenizer

The Contract Tokenizer is responsible for preprocessing legal contract text before analysis.

Features:
- Removes unnecessary whitespace and formatting inconsistencies
- Splits contract text into individual tokens
- Preserves punctuation for legal text analysis
- Prepares contract data for inference and classification

Example:

Input:
"This Agreement, effective June 2026."

Output:
["This", "Agreement", ",", "effective", "June", "2026", "."]

### Contract Inference Engine

The Contract Inference Engine analyzes tokenized contract text and extracts useful metadata.

Current Capabilities:
- Contract type identification
- Token count analysis
- Metadata extraction
- Basic contract classification

Supported Contract Types:
- Non-Disclosure Agreement (NDA)
- Service Agreement
- Employment Agreement

### Week 2 Processing Flow

Contract Text
→ Text Cleaning
→ Tokenization
→ Inference Engine
→ Contract Classification
→ Metadata Extraction

### Week 2 Outcome

The Week 2 implementation establishes the NLP foundation for intelligent contract understanding and prepares the system for future AI-based legal document analysis.

## Technologies Used

- Python
- FastAPI
- Regular Expressions (Regex)
- NLP Concepts
- Git & GitHub
