from fastapi.testclient import TestClient
from system_monitor import app

client = TestClient(app)

def test_cpu_endpoint():
    response = client.get("/cpu")
    assert response.status_code == 200
    assert "cpu" in response.json()
    assert isinstance(response.json()["cpu"], (int, float))

def test_memory_endpoint():
    response = client.get("/memory")
    assert response.status_code == 200
    assert "memory" in response.json()
    assert isinstance(response.json()["memory"], (int, float))

def test_disk_endpoint():
    response = client.get("/disk")
    assert response.status_code == 200
    assert "disk" in response.json()
    assert isinstance(response.json()["disk"], (int, float))