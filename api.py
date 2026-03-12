# api.py
from fastapi import FastAPI
from pydantic import BaseModel
from engine_api import analyze_market

app = FastAPI()

class AnalyzeRequest(BaseModel):
    symbol: str
    timeframe: str
    note: str | None = None

@app.post("/analyze")
def analyze(req: AnalyzeRequest):
    result = analyze_market(req.symbol, req.timeframe, req.note)
    return result  # result harus berupa dict/list yang bisa jadi JSON
