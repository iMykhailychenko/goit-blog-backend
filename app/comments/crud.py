from typing import List

from db import database
from app.comments.schemas import NewCommentBody, UpdateCommentBody, Comment


async def select_comments(post_id: int, limit: int, page: int) -> List[dict]:
    offset = (page - 1) * limit
    query = """
    SELECT * 
    FROM comments 
    WHERE comments.post_id = :post_id
    ORDER BY created_at DESC
    LIMIT :limit 
    OFFSET :offset"""
    return await database.fetch_all(query=query, values={"post_id": post_id, "limit": limit, "offset": offset})


async def count_total_comments(post_id: int) -> int:
    query = """SELECT count(*) FROM comments  WHERE comments.post_id = :post_id"""
    count = await database.fetch_one(query=query, values={"post_id": post_id})
    return int(count["count"]) if count else 0


async def find_comment(comment_id: int) -> dict:
    query = """SELECT * FROM comments WHERE comments.id = :id"""
    return await database.fetch_one(query=query, values={"id": comment_id})


@database.transaction()
async def create_comment(post_id: int, body: NewCommentBody) -> dict:
    query = """
    INSERT INTO comments (
        content,
        post_id
    )
    VALUES (
        :content,
        :post_id
    )
    RETURNING id
    """

    values = {
        "content": body.content,
        "post_id": post_id
    }

    comment_id = await database.execute(query, values=values)
    return await find_comment(comment_id)


async def delete_comment(comment_id: int) -> None:
    query = """
    DELETE FROM comments 
    WHERE comments.id = :id"""

    await database.execute(query, values={"id": comment_id})


@database.transaction()
async def update_comment(comment_id: int, old_comment_data: dict, new_comment_data: UpdateCommentBody) -> dict:
    old_comment_model = Comment(**old_comment_data)
    updated_comment = old_comment_model.copy(update=new_comment_data.dict(exclude_none=True))

    query = """
    UPDATE comments
    SET
        content = :content,
        updated_at = CURRENT_TIMESTAMP
    WHERE comments.id = :id    
    """

    values = {
        "id": comment_id,
        "content": updated_comment.content,
    }

    await database.execute(query=query, values=values)
    return await find_comment(comment_id=comment_id)
