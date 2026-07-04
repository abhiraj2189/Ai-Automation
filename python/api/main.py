from fastapi import FastAPI
from python.api.routes import router
from python.auth.auth_router import router as auth_router
from python.database.database import Database

app = FastAPI(
    title="AI Automation API",
    version="1.0.0"
)

@app.on_event("startup")
def startup_event():
    db = Database()
    db.create_tables()
    db.close()

app.include_router(router)
app.include_router(auth_router)

@app.get("/")
def home():
    return {"status": "Running"}