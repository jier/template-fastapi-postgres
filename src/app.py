from fastapi import FastAPI
from routes.users_route import app as UsersRouter

app = FastAPI()
app.include_router(UsersRouter)
