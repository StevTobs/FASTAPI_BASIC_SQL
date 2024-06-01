
from typing import List
import datetime as _dt
import pydantic as _pydantic 

class _PostBase(_pydantic.BaseModel):
    title: str
    content: str
    # Example of this class
    # {
    #     "title":"this is a title",
    #     "content":"some content for the post"
    # }

class PostCreate(_PostBase):
    pass

class Post(_PostBase):
    # Example of this class
    # {
    #     "id": 1
    #     "owner_id": 23
    #     "title":"this is a title",
    #     "content":"some content for the post"
    #     "date_created" : "12-12-12"
    #     "date_last_updated" : "30-12-12"
    # }

    id: int
    owner_id: int
    date_created: _dt.datetime
    date_last_updated: _dt.datetime

    #The reason to set this part because by default SQLAlchemy lazy loding ['orm_mode = False'] and we will not see user.post relationship
    class Config:
        orm_mode = True
        
class _UserBase(_pydantic.BaseModel):
    email: str

class UserCreate(_UserBase):
    password: str
    
class User(_UserBase):
    id: int
    is_active: bool
    posts: List[Post] = []

    class Config:
        #again, we don't want the lazy loding
        orm_mode = True
    