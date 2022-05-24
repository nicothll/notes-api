from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from notes_api.settings import CONFIG
from notes_api.models.note import Note

app = FastAPI(title="Notes-API")

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def init_app():
    app.db = AsyncIOMotorClient(CONFIG.mongo_uri).notesdb
    await init_beanie(app.db, document_models=[Note])
