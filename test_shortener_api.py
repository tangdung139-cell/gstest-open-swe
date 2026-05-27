from fastapi.testclient import TestClient
from shortener_api import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the URL Shortener API!"}

def test_shorten_url():
    payload = {"url": "https://example.com"}
    response = client.post("/shorten", json=payload)
    assert response.status_code == 200
    json_data = response.json()
    assert "short_url" in json_data
    assert json_data["original_url"] == "https://example.com"

def test_redirect_to_original():
    payload = {"url": "https://example.com"}
    shorten_response = client.post("/shorten", json=payload)
    short_url = shorten_response.json()["short_url"]

    redirect_response = client.get(f"/{short_url}")
    assert redirect_response.status_code == 200
    assert redirect_response.json() == {"original_url": "https://example.com"}

def test_short_url_not_found():
    response = client.get("/nonexistent")
    assert response.status_code == 404
    assert response.json() == {"detail": "Short URL not found"}