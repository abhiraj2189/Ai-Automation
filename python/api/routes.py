import json
from pathlib import Path
from fastapi import APIRouter, HTTPException
from fastapi import APIRouter, HTTPException, Query

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
    return load_json("ai_tools", "ai_tools.json")


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