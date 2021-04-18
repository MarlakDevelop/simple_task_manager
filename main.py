from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.database import database, metadata, engine
from apis.v1.rest import tasks_router
from core import settings


app = FastAPI()
metadata.create_all(engine)
app.state.database = database


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()

app.include_router(tasks_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS_WHITELIST,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)