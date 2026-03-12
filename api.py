from fastapi import FastAPI
from pydantic import BaseModel
from engine_api import analyze_market  # ini engine dummy barusan

app = FastAPI()

class AnalyzeRequest(BaseModel):
    symbol: str
    timeframe: str
    note: str | None = None

@app.get("/")
def root():
    return {"status": "ok", "message": "Chronos API is running"}

@app.post("/analyze")
def analyze(req: AnalyzeRequest):
    result = analyze_market(req.symbol, req.timeframe, req.note)
    return result
