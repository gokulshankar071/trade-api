import os
from fastapi import Header, HTTPException

API_TOKEN = os.getenv("API_TOKEN")

async def verify_token(x_token: str = Header(...)):
    if x_token != API_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid API Token")