from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
import hashlib

app = FastAPI()

# In-memory storage for URL mappings (for simplicity, using dict)
url_mapping: Dict[str, str] = {}

class URLRequest(BaseModel):
    url: str

@app.get("/")
async def root():
    return {"message": "Welcome to the URL Shortener API!"}

@app.post("/shorten")
async def shorten_url(request: URLRequest):
    original_url = request.url

    # Generate a simple hash for the short URL
    short_url_hash = hashlib.md5(original_url.encode()).hexdigest()[:6]

    # Store the mapping
    url_mapping[short_url_hash] = original_url

    return {"short_url": short_url_hash, "original_url": original_url}

@app.get("/{short_url}")
async def redirect_to_original(short_url: str):
    original_url = url_mapping.get(short_url)

    if not original_url:
        raise HTTPException(status_code=404, detail="Short URL not found")

    return {"original_url": original_url}