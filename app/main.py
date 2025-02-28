from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World 3"}

@app.get("/health")
def read_health():
    return {"status": "healthy"}
