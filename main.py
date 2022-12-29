import uvicorn
import db

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.long import long
from app.posts import posts
from app.comments import comments

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router)
app.include_router(long.router)
app.include_router(comments.router)


@app.on_event("startup")
async def startup() -> None:
    await db.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    await db.disconnect()


if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, host="0.0.0.0", reload=True)
