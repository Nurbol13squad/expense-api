import json
from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

DATA_FILE = Path("expenses.json")

expenses = []

class Expense(BaseModel):
    amount: float
    category: str
    
def load_expenses():
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text())
    return []

def save_expenses(expenses):
    DATA_FILE.write_text(json.dumps(expenses, indent=2))

@app.get("/")
def home():
    return {"message": "expense API is running"}

@app.post("/expenses")
def add_expenses(expense: Expense):
    expenses.append(expense.model_dump())
    save_expenses(expenses)
    return {"message": "Expense added", "expense": expense}

@app.get("/expenses")
def list_expenses():
    return load_expenses()


@app.get("/expenses/total")
def get_total():
    expenses = load_expenses()
    total = sum(e["amount"] for e in expenses)
    return {"total": reound(total, 2)}

@app.get("/expenses/summry")
def get_summary():
    expenses = load_expenses()
    totals = {}
    for e in expenses:
        category = e["category"]
        totals[category] = totals.get(category, 0) + e["amount"]
    return totals