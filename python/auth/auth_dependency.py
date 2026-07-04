from fastapi import Header, HTTPException

from python.auth.jwt_handler import verify_token


def get_current_user(authorization: str = Header(None)):

    if authorization is None:

        raise HTTPException(
            status_code=401,
            detail="Authorization Header Missing"
        )

    if not authorization.startswith("Bearer "):

        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )

    token = authorization.split(" ")[1]

    return verify_token(token)