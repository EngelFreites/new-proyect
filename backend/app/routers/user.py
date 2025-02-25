from fastapi import APIRouter, HTTPException
from ..models.user import UserBase, User
from db import SessionDep
from sqlmodel import select

router = APIRouter(tags=["User"])

@router.get("/api/users", response_model=list[User], status_code=200)
async def get_all_users(session: SessionDep):
  
  users = session.exec(select(User)).all()
  return users


@router.get("/api/users/{user_id}", response_model=User)
async def get_one_user(user_id: int, session: SessionDep):

  user = session.get(User, user_id )

  if not user:
    raise HTTPException(status_code=404, detail="User not found")
  
  return user