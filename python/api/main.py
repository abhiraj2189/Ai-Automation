from fastapi import FastAPI
from python.api.routes import router

app = FastAPI(
    title="AI Automation API",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "project": "AI Automation",
        "status": "Running"
    }


@app.get("/health")
def health():
    return {
        "success": True
    }