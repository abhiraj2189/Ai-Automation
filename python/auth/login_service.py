from fastapi import HTTPException

from python.auth.auth_repository import AuthRepository
from python.security.hash_password import verify_password
from python.auth.jwt_handler import create_access_token


class LoginService:

    def login(self, user):

        repo = AuthRepository()

        db_user = repo.get_user(user.email)

        # User not found
        if db_user is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid Email or Password"
            )

        # Verify Password
        if not verify_password(user.password, db_user[3]):
            raise HTTPException(
                status_code=401,
                detail="Invalid Email or Password"
            )

        # Create JWT Token
        token = create_access_token({
            "id": db_user[0],
            "username": db_user[1],
            "email": db_user[2]
        })

        return {
            "message": "Login Successful",
            "access_token": token,
            "token_type": "Bearer"
        }