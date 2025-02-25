from fastapi import APIRouter
from ..models.user import UserBase, User
from db import SessionDep
from sqlmodel import select

router = APIRouter(tags=["User"])

@router.get("/api/users", response_model=list[User], status_code=200)
async def get_all_users(session: SessionDep):
  
  users = session.exec(select(User)).all()
  return users


