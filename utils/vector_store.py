
import chromadb
from chromadb.utils import embedding_functions

chroma_client = chromadb.Client()
default_ef = embedding_functions.DefaultEmbeddingFunction()
collection = chroma_client.get_or_create_collection(name="contracts", embedding_function=default_ef)

def index_contract(doc_id: str, text: str, metadata: dict):
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
    for idx, chunk in enumerate(chunks[:5]):
        collection.add(
            documents=[chunk],
            metadatas=[{"doc_id": doc_id, **metadata}],
            ids=[f"{doc_id}_chunk_{idx}"]
        )

def search_contracts(query: str, n_results: int = 2):
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )
    return results
