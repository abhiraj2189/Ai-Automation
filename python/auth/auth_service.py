from fastapi import HTTPException

from python.auth.auth_repository import AuthRepository
from python.security.hash_password import hash_password


class AuthService:

    def register(self, user):

        password = hash_password(user.password)

        repo = AuthRepository()

        try:
            repo.create_user(
                user.username,
                user.email,
                password
            )
        except ValueError as e:
            raise HTTPException(
                status_code=400,
                detail=str(e)
            )

        return {
            "message": "User Registered Successfully"
        }