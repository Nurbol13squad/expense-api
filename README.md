# Expense Tracker API

Asmall REST API for recording and summarizing personal exoenses,
built with python and FastAPI. Expenses are saved to a local JSON file

## Features

- Add an expense (amount and category)
- List all expenses
- Get the total of all expenses
- Get totals grouped by category
- Data is kept between restarts

## Setup

1. Clone the repository and open the folder
2. Create and activate a virtual environment:
python -m venv venv
venv\Scripts\Activate.ps1

3. Install the dependencies:
pip install -r requirements.txt

## Run

uvicorn main:app --reload
then open http://127.0.0.1:8000/docs to try the API in your browser