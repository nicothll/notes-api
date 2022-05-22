from pprint import pprint
from fastapi import APIRouter, Depends, Response

from notes_api.models.note import Note, Category

router = APIRouter(prefix="/notes", tags=["Note"])


@router.get("")
async def fetch_all_notes():
    response = await Note.find_all().to_list()
    pprint(response)

    return response


@router.get("/{id}", response_model=Note)
async def fetch_one_note(id: str):
    return await Note.get(id)
