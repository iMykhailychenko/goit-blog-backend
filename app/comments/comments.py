from fastapi import APIRouter, HTTPException, Response

from utils import pagination
from app.comments import crud
from app.posts.crud import find_post
from app.comments.schemas import CommentList, Comment, NewCommentBody, UpdateCommentBody

router = APIRouter(
    prefix="",
    tags=["comments"],
)


@router.get("/posts/{post_id}/comments", response_model=CommentList)
async def get_post_list(post_id: int, limit: int = 10, page: int = 1) -> CommentList:
    """Return comments list for single post (with pagination)"""
    posts = await crud.select_comments(post_id=post_id, limit=limit, page=page)
    total = await crud.count_total_comments(post_id=post_id)

    return CommentList(**pagination(data=posts, limit=limit, page=page, total=total))


@router.post("/posts/{post_id}/comments", response_model=Comment)
async def create_comment(post_id: int, body: NewCommentBody) -> Comment:
    """Create new comment"""
    post = await find_post(post_id)

    if not post:
        raise HTTPException(status_code=404, detail=f"Post with id {post_id} does not exist", )

    comment = await crud.create_comment(post_id, body)
    return Comment(**comment)


@router.get("/comments/{comment_id}", response_model=Comment)
async def get_single_comment(comment_id: int) -> Comment:
    """Return single comment by ID"""
    comment = await crud.find_comment(comment_id)
    return Comment(**comment)


@router.delete("/comments/{comment_id}", status_code=204)
async def delete_comment(comment_id: int) -> Response:
    """Delete comment by ID"""
    post = await crud.find_comment(comment_id=comment_id)

    if not post:
        raise HTTPException(status_code=404, detail=f"Comment with id {comment_id} does not exist", )

    await crud.delete_comment(comment_id)
    return Response(status_code=204)


@router.put("/comments/{comment_id}", response_model=Comment)
async def update_comment(comment_id: int, body: UpdateCommentBody) -> Comment:
    """Overwrite comment information with new data"""
    comment = await crud.find_comment(comment_id)

    if not comment:
        raise HTTPException(status_code=404, detail=f"Comment with id {comment_id} does not exist", )

    new_comment = await crud.update_comment(comment_id=comment_id, old_comment_data=comment, new_comment_data=body)
    return Comment(**new_comment)
