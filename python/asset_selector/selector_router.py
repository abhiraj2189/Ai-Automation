from fastapi import APIRouter

from python.asset_selector.models import SelectorRequest

from python.asset_selector.selector_service import SelectorService


router = APIRouter(

    prefix="/selector",

    tags=["Asset Selector"]

)


@router.post("/")

def generate(

    data: SelectorRequest

):

    return SelectorService().generate(

        data.keyword,

        data.videos

    )