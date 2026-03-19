from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import PlainTextResponse
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded

from app.auth import verify_token
from app.rate_limiter import limiter
from app.data_service import fetch_market_news
from app.ai_service import generate_market_report

app = FastAPI(title="Trade Opportunities API")

app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request, exc):
    return PlainTextResponse("Rate limit exceeded", status_code=429)

@app.get("/analyze/{sector}")
@limiter.limit("5/minute")
async def analyze_sector(
        request: Request,   # ⭐ VERY IMPORTANT ADD THIS
        sector: str,
        token: str = Depends(verify_token)
    ):

    if not sector.isalpha():
        raise HTTPException(status_code=400, detail="Invalid sector")

    news = await fetch_market_news(sector)

    if not news:
        raise HTTPException(status_code=404, detail="No data found")

    report = await generate_market_report(sector, news)

    return PlainTextResponse(report, media_type="text/markdown")