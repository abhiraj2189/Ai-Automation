from fastapi import APIRouter
from python.schemas.register_schema import RegisterSchema
from python.auth.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register")
def register(user: RegisterSchema):

    service = AuthService()

    return service.register(user)