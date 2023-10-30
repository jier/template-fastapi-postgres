from fastapi.routing import APIRouter
from ..schemas.user_schema import User, UserCreate

app = APIRouter(prefix="/users", tags=["Users"])


@app.get("/", response_model=list[User])
async def get_all_users():
    ...


@app.post("/")
async def create_user(input_user: UserCreate):
    ...
