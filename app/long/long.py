from time import sleep
from fastapi import APIRouter


router = APIRouter(
    prefix="/long",
    tags=["long"],
)


@router.get("", status_code=200)
async def get_long() -> str:
    """Long request, 4s timeout"""
    sleep(4)

    return "success"

