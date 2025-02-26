from fastapi import APIRouter, HTTPException
from ..models.user import UserBase, User, CreateUser
from db import SessionDep
from sqlmodel import select
import bcrypt

router = APIRouter(tags=["User"])

def hash_password(password : str) -> str:
  salt = bcrypt.gensalt()
  hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
  return hashed_password

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

@router.post('/api/users', response_model= UserBase)
async def create_user(user_data: CreateUser, session: SessionDep ):
  user_db = user_data.model_dump()
  password = user_data.password
  hashed_password = hash_password(password)

  user = User(**user_db, hashed_password= hashed_password )

  session.add(user)
  session.commit()
  session.refresh(user)

  return user 

@router.delete("/api/users/{user_id}")
async def delete_user(user_id: int, session: SessionDep):
  
  user = session.get(User, user_id )

  if not user:
    raise HTTPException(status_code=404, detail="User not found")
  
  session.delete(user)
  session.commit()

  return {"message": "User Deleted succefully"}