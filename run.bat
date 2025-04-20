@echo off

if not exist venv\ ( 
    python -m venv venv
)

call venv\Scripts\activate
if not exist requirements.txt (
    echo Error: requirements.txt not found!
    pause
    exit /b 1
)

python -m pip install --upgrade pip
pip install -r requirements.txt

python app.py

pause