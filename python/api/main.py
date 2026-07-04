from fastapi import FastAPI
from python.api.routes import router
from python.auth.auth_router import router as auth_router

app = FastAPI(
    title="AI Automation API",
    version="1.0.0"
)

app.include_router(router)
app.include_router(auth_router)

@app.get("/")
def home():
    return {"status": "Running"}