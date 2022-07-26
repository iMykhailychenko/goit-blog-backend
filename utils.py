from math import ceil
from typing import List

from pydantic import BaseModel


class PaginationSchema(BaseModel):
    data: List
    page: int
    limit: int
    total_items: int
    total_pages: int


def pagination(data: List, limit: int, page: int, total: int) -> dict:
    return {
        "data": data,
        "page": page,
        "limit": limit,
        "total_items": total,
        "total_pages": ceil(total / limit),
    }
