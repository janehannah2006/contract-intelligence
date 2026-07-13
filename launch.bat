@echo off
echo ===================================================
echo [1/2] Navigating to Project Root Directory...
cd /d C:\Users\Pranathi\contract_intelligence

echo [2/2] Launching AI Contract Server...
echo The browser dashboard will open automatically in 5 seconds.
echo ===================================================
start "" "http://127.0.0.1:8000/"
uvicorn app.main:app --reload
pause