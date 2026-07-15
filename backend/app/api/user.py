from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from fastapi import HTTPException
from app.db.session import get_db
from app.schemas.user import UserRegister
from app.models.user import User
from app.core.security import hash_password
from app.schemas.user import UserLogin
from app.core.jwt import create_access_token
from app.core.security import verify_password
from app.core.deps import get_current_user
router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/register")
def register(data: UserRegister, db: Session = Depends(get_db)):

    # ① 查询用户名是否已经存在
    exists = db.scalar(
        select(User).where(User.username == data.username)
    )

    if exists:
        return {
            "message": "用户名已存在"
        }

    # ② 用户不存在，创建新用户
    user = User(
        username=data.username,
        password=hash_password(data.password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return {
        "id": user.id,
        "username": user.username
    }

@router.post("/login")
def login(data: UserLogin, db: Session = Depends(get_db)):

    user = db.scalar(
        select(User).where(User.username == data.username)
    )

    if not user:
        return {
            "message": "用户名不存在"
        }

    if not verify_password(
        data.password,
        user.password
    ):
        return {
            "message": "密码错误"
        }

    token = create_access_token(
        user.username
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@router.get("/me")
def get_me(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "username": current_user.username,
    }