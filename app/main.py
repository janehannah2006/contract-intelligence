
import os
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from utils.nlp_engine import extract_text_from_pdf, analyze_contract
from utils.vector_store import index_contract, search_contracts

app = FastAPI(title="AI Contract Intelligence Platform")

OS_DATA_DIR = "data"
if not os.path.exists(OS_DATA_DIR):
    os.makedirs(OS_DATA_DIR)

@app.post("/upload/")
async def upload_contract(file: UploadFile = File(...)):
    file_path = os.path.join(OS_DATA_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
        
    raw_text = extract_text_from_pdf(file_path)
    analysis = analyze_contract(raw_text)
    index_contract(doc_id=file.filename, text=raw_text, metadata={"filename": file.filename})
    
    return {
        "filename": file.filename,
        "status": "Processed and Indexed Successfully",
        "analysis": analysis
    }

@app.get("/search/")
async def query_contracts(q: str):
    search_res = search_contracts(q)
    return {"query": q, "matches": search_res['documents']}

@app.get("/", response_class=HTMLResponse)
async def main_page():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Contract Intelligence Portal</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f6f9; color: #333; }
            .container { max-width: 800px; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
            h1 { color: #2c3e50; }
            .box { border: 1px solid #ddd; padding: 20px; border-radius: 4px; margin-bottom: 20px; background: #fafafa; }
            input[type="submit"], button { background: #3498db; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer; }
            input[type="submit"]:hover { background: #2980b9; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>AI Contract Intelligence Dashboard</h1>
            <hr>
            <div class="box">
                <h3>1. Ingest Contract (PDF)</h3>
                <form action="/upload/" enctype="multipart/form-data" method="post">
                    <input name="file" type="file" accept=".pdf" required><br><br>
                    <input type="submit" value="Analyze & Index Contract">
                </form>
            </div>
            <div class="box">
                <h3>2. Semantic Risk Search</h3>
                <form action="/search/" method="get">
                    <input type="text" name="q" placeholder="e.g., auto-renewal or liability limits" style="width: 70%; padding: 8px;">
                    <button type="submit">Search Clauses</button>
                </form>
            </div>
        </div>
    </body>
    </html>
    """
