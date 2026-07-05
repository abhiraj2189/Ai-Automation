from fastapi import APIRouter, Depends

from python.auth.auth_dependency import get_current_user
from python.dashboard.dashboard_service import DashboardService

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("")
def dashboard(
    user=Depends(get_current_user)
):

    service = DashboardService()

    return service.get_dashboard(user)