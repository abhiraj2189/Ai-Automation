from python.auth.auth_repository import AuthRepository
from python.security.hash_password import hash_password


class AuthService:

    def register(self, user):

        password = hash_password(user.password)

        repo = AuthRepository()

        repo.create_user(
            user.username,
            user.email,
            password
        )

        return {
            "message": "User Registered Successfully"
        }