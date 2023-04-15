from fastapi import APIRouter, Response

from ..models.note import Note

router = APIRouter(prefix="/api/notes", tags=["Note"])


@router.get("")
async def fetch_all_notes():
    response = await Note.find_all().to_list()
    return response


@router.post("")
async def create_note(note: Note):
    response = await note.insert()
    return Response(status_code=201, content=str(response))


@router.get("/{id}", response_model=Note)
async def fetch_one_note(id: str):
    return await Note.get(id)


@router.put("/{id}", response_model=Note)
async def update_note(id: str, data: dict):
    note = await Note.get(id)
    if data.get("_id"):
        del data["_id"]
    await note.set(data)
    return note


@router.delete("/{id}", response_model=Note)
async def remove_note(id: str):
    note = await Note.get(id)
    await note.delete()
    return Response(status_code=204)
