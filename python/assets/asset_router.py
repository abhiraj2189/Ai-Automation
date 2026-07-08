from fastapi import APIRouter

from python.assets.models import AssetRequest

from python.assets.asset_service import AssetService


router = APIRouter(

    prefix="/assets",

    tags=["Assets"]

)


@router.post("/")

def generate(data: AssetRequest):

    service = AssetService()

    return service.generate(

        data.keyword,

        data.count

    )