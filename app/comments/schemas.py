from datetime import datetime

from typing import Optional, List
from pydantic import BaseModel

from utils import PaginationSchema


class Comment(BaseModel):
    id: int
    post_id: int
    content: str
    created_at: datetime
    updated_at: Optional[datetime]


class CommentList(PaginationSchema):
    data: List[Comment]


class NewCommentBody(BaseModel):
    content: str


class UpdateCommentBody(BaseModel):
    content: Optional[str]
