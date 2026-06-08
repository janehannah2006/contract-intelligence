from fastapi import FastAPI, UploadFile, File
import pdfplumber
import os

app = FastAPI()

# Create uploads folder if it doesn't exist
os.makedirs("uploads", exist_ok=True)

@app.get("/")
def home():
    return {
        "message": "AI Contract Intelligence Project Running"
    }

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    # Save uploaded file
    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    text = ""
    total_pages = 0

    # Read PDF
    with pdfplumber.open(file_path) as pdf:

        total_pages = len(pdf.pages)

        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return {
        "filename": file.filename,
        "pages": total_pages,
        "characters": len(text),
        "text": text[:1000]
    }