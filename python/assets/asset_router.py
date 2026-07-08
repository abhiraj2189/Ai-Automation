from fastapi import APIRouter

from python.assets.asset_schema import AssetRequest
from python.assets.asset_service import AssetService

router = APIRouter(
    prefix="/assets",
    tags=["Assets"]
)


@router.post("/")
def generate(data: AssetRequest):

    service = AssetService()

    return {
        "success": True,
        "assets": service.generate_assets(data.scenes)
    }