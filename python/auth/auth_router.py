from fastapi import APIRouter

from python.schemas.register_schema import RegisterSchema
from python.schemas.login_schema import LoginSchema

from python.auth.auth_service import AuthService
from python.auth.login_service import LoginService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(user: RegisterSchema):

    service = AuthService()

    return service.register(user)


@router.post("/login")
def login(user: LoginSchema):

    service = LoginService()

    return service.login(user)