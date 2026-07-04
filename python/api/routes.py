import json
from pathlib import Path
from fastapi import APIRouter, HTTPException
from fastapi import APIRouter, HTTPException, Query
from python.services.ai_tools_service import AIToolsService

router = APIRouter()

# Project Root
ROOT_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = ROOT_DIR / "data"


def load_json(folder, filename):
    file_path = DATA_DIR / folder / filename

    if not file_path.exists():
        raise HTTPException(status_code=404, detail=f"{filename} not found")

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


@router.get("/ai-tools")
def get_ai_tools():

    service = AIToolsService()

    return service.get_tools()


@router.get("/coding")
def get_coding_news():
    return load_json("coding", "coding_news.json")


@router.get("/github/user")
def get_github_user():
    return load_json("github", "user.json")


@router.get("/github/repos")
def get_github_repositories():
    return load_json("github", "repositories.json")
@router.get("/ai-tools/search")
def search_ai_tools(keyword: str = Query(...)):

    data = load_json("ai_tools", "ai_tools.json")

    result = []

    keyword = keyword.lower()

    for item in data:

        text = str(item).lower()

        if keyword in text:
            result.append(item)

    return {
        "total": len(result),
        "results": result
    }
def search_data(data, keyword):
    keyword = keyword.lower()
    result = []

    for item in data:
        if keyword in str(item).lower():
            result.append(item)

    return result
@router.get("/analytics")
def get_analytics():
    return load_json("analytics", "analytics.json")
@router.get("/search")
def global_search(keyword: str):

    ai_tools = load_json("ai_tools", "ai_tools.json")
    coding = load_json("coding", "coding_news.json")

    try:
        github = load_json("github", "repositories.json")
    except:
        github = []

    try:
        news = load_json("news", "ai_news.json")
    except:
        news = []

    return {
        "ai_tools": search_data(ai_tools, keyword),
        "coding_news": search_data(coding, keyword),
        "github": search_data(github, keyword),
        "ai_news": search_data(news, keyword)
    }
from fastapi import Depends
from python.auth.auth_dependency import get_current_user


@router.get("/profile")
def profile(user=Depends(get_current_user)):

    return {
        "message": "Welcome",
        "user": user
    }