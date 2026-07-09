from fastapi import APIRouter

from python.asset_planner.models import PlannerRequest

from python.asset_planner.planner_service import PlannerService


router = APIRouter(

    prefix="/planner",

    tags=["AI Planner"]

)


@router.post("/")

def generate(

    data: PlannerRequest

):

    return PlannerService().generate(

        data.scenes

    )