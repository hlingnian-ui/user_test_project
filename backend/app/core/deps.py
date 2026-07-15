from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.jwt import verify_token
from app.db.session import get_db
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):
    payload = verify_token(token)

    if payload is None:
        raise HTTPException(status_code=401, detail="Token 无效")

    username = payload.get("sub")

    user = db.scalar(
        select(User).where(User.username == username)
    )

    if user is None:
        raise HTTPException(status_code=401, detail="用户不存在")

    return user