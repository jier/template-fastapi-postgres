from fastapi import Depends, Response
from fastapi.routing import APIRouter
from schemas.user_schema import User, UserCreate
from services import database_service as dbs
from sqlalchemy.orm import Session
from config.database_config import get_db

app = APIRouter(prefix="/users", tags=["Users"])


@app.get("/", response_model=list[User])
async def get_all_users(db: Session = Depends(get_db)):
    return dbs.get_all_users(db)


@app.post("/")
async def create_user(input_user: UserCreate):
    ...


@app.get("/{user_id}", response_model=User)
async def get_user_by_id(user_id: int, db=Depends(get_db)):
    result = dbs.get_user_by_id(db, user_id)
    return result if result else Response(status_code=404)
