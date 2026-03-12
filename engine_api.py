# engine_api.py

def analyze_market(symbol: str, timeframe: str, note: str | None = None):
    # Nanti kamu ganti isi fungsi ini pakai logic beneran
    return {
        "symbol": symbol,
        "timeframe": timeframe,
        "bias": "long",
        "rr": 2.5,
        "tp": 12345,
        "sl": 12000,
        "note": note or ""
    }
