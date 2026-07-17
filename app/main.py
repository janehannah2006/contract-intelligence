import os
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from utils.nlp_engine import analyze_contract, extract_text_from_pdf
from utils.vector_store import index_contract, search_contracts
app = FastAPI(title="Contract Risk Analyzer API")
OS_DATA_DIR = "data"
if not os.path.exists(OS_DATA_DIR):
    os.makedirs(OS_DATA_DIR)
@app.post("/upload/")
async def upload_contract(file: UploadFile = File(...)):
    """Handles PDF uploads, parses text, runs analysis pipelines, and indexes data."""
    file_path = os.path.join(OS_DATA_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Process document text layers
    raw_text = extract_text_from_pdf(file_path)

    # Machine learning evaluation step
    analysis = analyze_contract(raw_text)

    # Local vector indexing
    index_contract(
        doc_id=file.filename, text=raw_text, metadata={"filename": file.filename}
    )

    return {
        "filename": file.filename,
        "status": "Processed and Indexed Successfully",
        "analysis": analysis,
    }
@app.get("/search/")
async def query_contracts(q: str):
    """Queries indexed document storage for semantic keyword matches."""
    search_res = search_contracts(q)
    return {"query": q, "matches": search_res["documents"]}
@app.get("/", response_class=HTMLResponse)
async def main_page():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Contract Risk Analyzer</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght=400;500;600;700&display=swap" rel="stylesheet">
        <script src="https://unpkg.com/lucide@latest"></script>
        <style>
            body { font-family: 'Inter', sans-serif; background-color: #0b0f19; }
            .panel-bg { background-color: #111827; border: 1px solid #1f2937; }
        </style>
    </head>
    <body class="text-gray-200 min-h-screen flex flex-col">

        <!-- Top Navigation -->
        <header class="border-b border-gray-800 bg-gray-900/80 backdrop-blur sticky top-0 z-50">
            <div class="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">
                <div class="flex items-center space-x-3">
                    <div class="p-2 bg-indigo-600 rounded-lg">
                        <i data-lucide="file-text" class="w-5 h-5 text-white"></i>
                    </div>
                    <div>
                        <span class="text-base font-bold tracking-wide text-white">Contract Intelligence Platform</span>
                        <p class="text-xs text-gray-400">Internal Audit Dashboard</p>
                    </div>
                </div>
                <div class="text-xs text-gray-400 flex items-center bg-gray-800/60 px-3 py-1.5 rounded-full border border-gray-700">
                    <span class="h-2 w-2 rounded-full bg-green-500 mr-2 animate-pulse"></span>
                    Local Analytics Active
                </div>
            </div>
        </header>

        <!-- Main Dashboard Layout -->
        <main class="flex-1 max-w-7xl w-full mx-auto p-6 grid grid-cols-1 lg:grid-cols-12 gap-6">
            
            <!-- Controls Sidebar Column -->
            <section class="lg:col-span-5 space-y-6">
                
                <!-- PDF Document Upload Form Card -->
                <div class="panel-bg p-6 rounded-xl shadow-sm">
                    <div class="flex items-center space-x-2 mb-3">
                        <i data-lucide="upload" class="w-4 h-4 text-indigo-400"></i>
                        <h2 class="text-sm font-semibold text-white">Upload New Contract</h2>
                    </div>
                    <p class="text-xs text-gray-400 mb-4">Select and submit a standard PDF legal document to extract entities and calculate compliance flags.</p>
                    
                    <form id="uploadForm" class="space-y-4">
                        <label class="border border-dashed border-gray-700 hover:border-indigo-500 transition-colors rounded-lg p-6 flex flex-col items-center justify-center cursor-pointer bg-gray-900/40 group">
                            <i data-lucide="cloud-lightning" class="w-8 h-8 text-gray-500 group-hover:text-indigo-400 transition-colors mb-2"></i>
                            <span class="text-xs font-medium text-gray-300" id="fileLabel">Select contract file (PDF)</span>
                            <input type="file" id="contractFile" name="file" accept=".pdf" class="hidden" onchange="handleFileChange()">
                        </label>
                        
                        <button type="button" onclick="submitContractFile()" class="w-full bg-indigo-600 hover:bg-indigo-500 text-white font-medium text-xs py-2.5 px-4 rounded-lg transition-colors flex items-center justify-center space-x-2">
                            <span>Analyze Document</span>
                            <i data-lucide="chevron-right" class="w-3.5 h-3.5"></i>
                        </button>
                    </form>
                </div>

                <!-- Database Semantic Search Form Card -->
                <div class="panel-bg p-6 rounded-xl shadow-sm">
                    <div class="flex items-center space-x-2 mb-3">
                        <i data-lucide="search" class="w-4 h-4 text-green-400"></i>
                        <h2 class="text-sm font-semibold text-white">Search Document Clauses</h2>
                    </div>
                    <p class="text-xs text-gray-400 mb-4">Query your localized vector store using descriptive terms to scan risk matching scores.</p>
                    
                    <div class="flex space-x-2">
                        <input type="text" id="searchTerm" placeholder="e.g., liability limits, data leaks" class="flex-1 bg-gray-950 border border-gray-800 rounded-lg px-3 py-2 text-xs text-gray-200 focus:outline-none focus:border-green-500 transition-colors">
                        <button type="button" onclick="submitSearchQuery()" class="bg-green-600 hover:bg-green-500 text-white font-medium text-xs px-4 rounded-lg transition-colors flex items-center space-x-1">
                            <span>Search</span>
                        </button>
                    </div>
                </div>

                <!-- System Metadata Context Details -->
                <div class="panel-bg p-5 rounded-xl shadow-sm">
                    <div class="flex items-center space-x-2 mb-3">
                        <i data-lucide="settings" class="w-4 h-4 text-gray-400"></i>
                        <h2 class="text-sm font-semibold text-white">System Information</h2>
                    </div>
                    <div class="space-y-2.5 text-xs">
                        <div class="flex justify-between items-center text-gray-400">
                            <span>Named Entity Engine</span>
                            <span class="font-mono bg-gray-800 px-2 py-0.5 rounded text-gray-300">spaCy (en_core_web_sm)</span>
                        </div>
                        <div class="flex justify-between items-center text-gray-400">
                            <span>Risk Classifier Model</span>
                            <span class="font-mono bg-gray-800 px-2 py-0.5 rounded text-gray-300">bart-large-mnli</span>
                        </div>
                        <div class="flex justify-between items-center text-gray-400">
                            <span>Vector Index Store</span>
                            <span class="font-mono bg-gray-800 px-2 py-0.5 rounded text-gray-300">ChromaDB</span>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Interactive Results Stream Column -->
            <section class="lg:col-span-7 flex flex-col">
                <div class="panel-bg p-6 rounded-xl shadow-sm flex-1 flex flex-col min-h-[450px]">
                    <div class="flex items-center justify-between border-b border-gray-800 pb-3 mb-4">
                        <div class="flex items-center space-x-2">
                            <i data-lucide="terminal" class="w-4 h-4 text-indigo-400"></i>
                            <h2 class="text-sm font-semibold text-white">JSON Output Console</h2>
                        </div>
                        <button onclick="resetConsole()" class="text-xs text-gray-500 hover:text-gray-300 flex items-center space-x-1">
                            <i data-lucide="refresh-cw" class="w-3 h-3"></i>
                            <span>Clear</span>
                        </button>
                    </div>

                    <!-- App Request Status Progress Loader -->
                    <div id="loadingStatus" class="hidden flex-1 flex flex-col items-center justify-center space-y-2 text-gray-400">
                        <div class="animate-spin rounded-full h-6 w-6 border-2 border-indigo-500 border-t-transparent"></div>
                        <p class="text-xs">Processing data models, please wait...</p>
                    </div>

                    <!-- Dynamic Output Box Terminal Frame -->
                    <div id="terminalLog" class="flex-1 bg-gray-950 rounded-lg p-4 font-mono text-xs overflow-y-auto max-h-[500px] text-green-400">
                        <span class="text-gray-500">// System ready. Waiting for file upload or database query...</span>
                    </div>
                </div>
            </section>
        </main>

        <script>
            // Generate graphics
            lucide.createIcons();

            function handleFileChange() {
                const input = document.getElementById('contractFile');
                const label = document.getElementById('fileLabel');
                if (input.files.length > 0) {
                    label.textContent = input.files[0].name;
                    label.className = "text-xs font-semibold text-indigo-400";
                }
            }

            function resetConsole() {
                document.getElementById('terminalLog').innerHTML = '<span class="text-gray-500">// System ready. Waiting for file upload or database query...</span>';
                document.getElementById('contractFile').value = '';
                document.getElementById('searchTerm').value = '';
                document.getElementById('fileLabel').textContent = 'Select contract file (PDF)';
                document.getElementById('fileLabel').className = 'text-xs font-medium text-gray-300';
            }

            async function submitContractFile() {
                const input = document.getElementById('contractFile');
                if (input.files.length === 0) {
                    alert('Please select a PDF file before continuing.');
                    return;
                }

                const payload = new FormData();
                payload.append('file', input.files[0]);

                const spinner = document.getElementById('loadingStatus');
                const log = document.getElementById('terminalLog');

                log.classList.add('hidden');
                spinner.classList.remove('hidden');

                try {
                    const res = await fetch('/upload/', {
                        method: 'POST',
                        body: payload
                    });
                    const resData = await res.json();
                    log.innerHTML = '<pre class="bg-transparent">' + JSON.stringify(resData, null, 4) + '</pre>';
                } catch (err) {
                    log.innerHTML = `<span class="text-red-400">// Connection error occurred: ${err.message}</span>`;
                } finally {
                    spinner.classList.add('hidden');
                    log.classList.remove('hidden');
                }
            }

            async function submitSearchQuery() {
                const query = document.getElementById('searchTerm').value.trim();
                if (!query) {
                    alert('Please provide a search term.');
                    return;
                }

                const spinner = document.getElementById('loadingStatus');
                const log = document.getElementById('terminalLog');

                log.classList.add('hidden');
                spinner.classList.remove('hidden');

                try {
                    const res = await fetch(`/search/?q=${encodeURIComponent(query)}`);
                    const resData = await res.json();
                    log.innerHTML = '<pre class="bg-transparent">' + JSON.stringify(resData, null, 4) + '</pre>';
                } catch (err) {
                    log.innerHTML = `<span class="text-red-400">// Query error occurred: ${err.message}</span>`;
                } finally {
                    spinner.classList.add('hidden');
                    log.classList.remove('hidden');
                }
            }
        </script>
    </body>
    </html>
    """
