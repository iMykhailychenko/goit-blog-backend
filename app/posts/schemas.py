from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel
from utils import PaginationSchema


class Post(BaseModel):
    id: int
    title: str
    content: str
    image: str
    views: int
    preview_image: str
    created_at: datetime
    updated_at: Optional[datetime]


class PostsList(PaginationSchema):
    data: List[Post]


class NewPostBody(BaseModel):
    title: str
    content: str
    image: str
    preview_image: str


class UpdatePostBody(BaseModel):
    title: Optional[str]
    content: Optional[str]
    image: Optional[str]
    preview_image: Optional[str]
