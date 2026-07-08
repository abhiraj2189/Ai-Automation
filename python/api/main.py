from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from python.api.routes import router
from python.auth.auth_router import router as auth_router
from python.database.database import Database
from python.favorites.favorites_router import router as favorites_router
from python.notes.notes_router import router as notes_router
from python.dashboard.dashboard_router import router as dashboard_router
from python.ai_chat.ai_chat_router import router as ai_chat_router
from python.chat.chat_router import router as chat_router
from python.research.research_router import router as research_router
from python.script.script_router import router as script_router
from python.scene.scene_router import router as scene_router
from python.studio.studio_router import router as studio_router
from python.projects.project_router import router as project_router
from python.assets.asset_router import router as asset_router
from python.voice.voice_router import router as voice_router

app = FastAPI(
    title="AI Automation API",
    version="1.0.0",
    description="AI Automation Backend"
)

# ==========================
# CORS
# ==========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================
# Startup
# ==========================
@app.on_event("startup")
def startup_event():
    db = Database()
    db.create_tables()
    db.close()

# ==========================
# Home
# ==========================
@app.get("/")
def home():
    return {
        "status": "Running 🚀",
        "message": "AI Automation Backend"
    }

# ==========================
# Routers
# ==========================
app.include_router(router)
app.include_router(auth_router)
app.include_router(favorites_router)
app.include_router(notes_router)
app.include_router(dashboard_router)
app.include_router(ai_chat_router)
app.include_router(chat_router)
app.include_router(research_router)
app.include_router(script_router)
app.include_router(scene_router)
app.include_router(studio_router)
app.include_router(project_router)
app.include_router(asset_router)
app.include_router(voice_router)