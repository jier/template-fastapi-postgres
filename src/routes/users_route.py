from fastapi import Depends
from fastapi.routing import APIRouter
from schemas.user_schema import User, UserCreate
from services import database_service as dbs
#from services.database_service import d
from config.database_config import get_db

app = APIRouter(prefix="/users", tags=["Users"])


@app.get("/", response_model=list[User])
async def get_all_users(db = Depends(get_db)):
    return dbs.get_all_users(db)


@app.post("/")
async def create_user(input_user: UserCreate):
    ...
