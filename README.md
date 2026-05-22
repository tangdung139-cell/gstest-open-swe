# Hello World API

This is a simple FastAPI application that serves a `Hello, World!` message and includes a health-check endpoint.

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

## Deployment

### Deployment on Local Machine
To deploy the API on a local environment:

1. Complete the installation steps mentioned above.
2. Start the API server using the following command:
   ```bash
   uvicorn hello_world_api:app --reload
   ```

The API will be deployed on `http://127.0.0.1:5000` by default.

### Deployment on a Server using Gunicorn
To run the API on a production server:

1. Install Gunicorn:
   ```bash
   pip install gunicorn
   ```
2. Run Gunicorn to serve the application:
   ```bash
   gunicorn -w 4 -b 0.0.0.0:8000 hello_world_api:app
   ```

The API will now be available at `http://<server-ip>:8000`.

## Running the API

Run the development server:

```bash
uvicorn hello_world_api:app --reload
```

The API will run on `http://127.0.0.1:8000`

## Endpoints

- **Health Check**: `GET /health`
   - Response: `{ "status": "ok" }`

- **Hello World**: `GET /`
   - Response: `{ "message": "Hello, World!" }`