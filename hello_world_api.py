from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get('/')
def hello_world():
    return JSONResponse(content={"message": "Hello, World!"})

@app.get('/health')
def health_check():
    return JSONResponse(content={"status": "ok"})

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)