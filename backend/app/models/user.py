from sqlmodel import SQLModel, Field

class UserBase(SQLModel):
  name: str = Field(default=None)
  age: int = Field(default=None)
  email: str =Field(default=None)


class CreateUser(UserBase):
  password: str

class User(UserBase, table=True):
  id: int = Field(default=None, primary_key=True) 
  hashed_password: str