from datetime import datetime, timedelta
from jose import JWTError, jwt
from jose import jwt

SECRET_KEY = "user_test_project_secret"

ALGORITHM = "HS256"

EXPIRE_MINUTES = 60


def create_access_token(username: str):
    expire = datetime.utcnow() + timedelta(minutes=EXPIRE_MINUTES)

    payload = {
        "sub": username,
        "exp": expire
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

def verify_token(token: str):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload
    except JWTError:
        return None