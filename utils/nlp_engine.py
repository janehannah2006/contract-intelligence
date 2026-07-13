
import pypdf
import spacy
from transformers import pipeline

# Load lighter spacy model for fast entity extraction
nlp = spacy.load("en_core_web_sm")

# Load a zero-shot classification pipeline for legal clause risk analysis
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def extract_text_from_pdf(pdf_path: str) -> str:
    text = ""
    with open(pdf_path, "rb") as f:
        reader = pypdf.PdfReader(f)
        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content + "\n"
    return text

def analyze_contract(text: str):
    doc = nlp(text[:5000]) # Process first 5000 chars for demo speed
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents if ent.label_ in ["DATE", "ORG", "MONEY"]]
    
    labels = ["High Risk Termination", "Standard Confidentiality", "Auto-Renewal Liability", "Indemnification"]
    chunks = [text[i:i+2000] for i in range(0, min(len(text), 6000), 2000)]
    risk_results = []
    
    for chunk in chunks:
        if len(chunk.strip()) > 100:
            res = classifier(chunk, candidate_labels=labels)
            for label, score in zip(res['labels'], res['scores']):
                if score > 0.6: 
                    risk_results.append({"clause_type": label, "confidence": round(score, 2), "snippet": chunk[:150] + "..."})
                    
    return {
        "extracted_entities": entities[:10],
        "risk_analysis": risk_results
    }
