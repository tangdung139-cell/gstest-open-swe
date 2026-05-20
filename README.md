# Hello World API

This is a simple Flask application that serves a `Hello, World!` message and includes a health-check endpoint.

## Installation

### Prerequisites

- Python 3.11+

### Steps

1. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the API

Run the development server:

```bash
python hello_world_api.py
```

The API will run on `http://127.0.0.1:5000`

## Endpoints

- **Health Check**: `GET /health`
   - Response: `{ "status": "ok" }`

- **Hello World**: `GET /`
   - Response: `{ "message": "Hello, World!" }`