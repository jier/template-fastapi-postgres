from schemas import user_schema
from models import user_model
from sqlalchemy.orm import Session

async def get_all_users(db: Session, skip:int = 0, limit:int=100) -> list[user_model.User]:
    return db.query(user_model.User).offset(skip).limit(limit).all()
    