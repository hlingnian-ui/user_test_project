from fastapi import FastAPI
from app.api.user import router as user_router
from app.db.database import Base, engine
from app.models.user import User
# 创建所有数据表
Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Test Project")

app.include_router(user_router)
@app.get("/")
def root():
    return {
        "message": "FastAPI + MySQL is running!"
    }