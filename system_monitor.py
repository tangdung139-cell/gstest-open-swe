from fastapi import FastAPI
from fastapi.responses import JSONResponse
import psutil

app = FastAPI()

@app.get("/cpu")
def get_cpu_usage():
    """Endpoint to get the CPU usage percentage."""
    cpu_usage = psutil.cpu_percent(interval=1)
    return JSONResponse(content={"cpu": cpu_usage})

@app.get("/memory")
def get_memory_usage():
    """Endpoint to get the memory usage percentage."""
    memory = psutil.virtual_memory()
    return JSONResponse(content={"memory": memory.percent})

@app.get("/disk")
def get_disk_usage():
    """Endpoint to get the disk usage percentage."""
    disk = psutil.disk_usage('/')
    return JSONResponse(content={"disk": disk.percent})