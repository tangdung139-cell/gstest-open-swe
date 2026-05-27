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

## Deployment

To deploy the URL Shortener project, you can use the following steps:

### Local Deployment

1. Install the required dependencies by following the installation instructions above.
2. Run the application using the command:
   ```bash
   uvicorn shortener_api:app --host 0.0.0.0 --port 8000 --reload
   ```
3. Access the application in your browser at `http://<YOUR_SERVER_IP>:8000`.

### Deployment to a Production Environment

1. Use a production-grade WSGI HTTP server like Gunicorn to deploy the app.
2. Install Gunicorn:
   ```bash
   pip install gunicorn
   ```
3. Run the application using Gunicorn:
   ```bash
   gunicorn -w 4 -k uvicorn.workers.UvicornWorker shortener_api:app
   ```
4. To deploy on a cloud platform, containerize the application using Docker:

   - Create a `Dockerfile` with the following content:
     ```dockerfile
     FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

     WORKDIR /app
     
     COPY . /app
     
     RUN pip install -r requirements.txt

     CMD ["uvicorn", "shortener_api:app", "--host", "0.0.0.0", "--port", "80"]
     ```
   
   - Build and run the Docker container:
     ```bash
     docker build -t url-shortener .
     docker run -d -p 80:80 url-shortener
     ```

5. Integrate with a domain name (optional): Use a reverse proxy like NGINX or a managed cloud service to map a custom domain to your application.

## Endpoints

- **Home**: `GET /`
   - Response: `{ "message": "Welcome to the URL Shortener API!" }`

- **Shorten URL**: `POST /shorten`
   - Request Body: `{ "url": "https://example.com" }`
   - Response: `{ "short_url": "abc123", "original_url": "https://example.com" }`

- **Redirect to Original**: `GET /{short_url}`
   - Path Parameter: `short_url` (e.g., `abc123`)
   - Response: `{ "original_url": "https://example.com" }`