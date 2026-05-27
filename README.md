# URL Shortener

This is a minimal URL Shortener project built using FastAPI. It allows users to generate short URLs and redirect them to their original destinations.

## Installation

### Prerequisites

- Python 3.10+

### Steps

1. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install required dependencies:
   ```bash
   pip install flask fastapi
   ```
## Running the URL Shortener

Run the development server:

```bash
uvicorn shortener_api:app --reload
```

The API will run on `http://127.0.0.1:8000`

## Endpoints

- **Home**: `GET /`
   - Response: `{ "message": "Welcome to the URL Shortener API!" }`

- **Shorten URL**: `POST /shorten`
   - Request Body: `{ "url": "https://example.com" }`
   - Response: `{ "short_url": "abc123", "original_url": "https://example.com" }`

- **Redirect to Original**: `GET /{short_url}`
   - Path Parameter: `short_url` (e.g., `abc123`)
   - Response: `{ "original_url": "https://example.com" }`