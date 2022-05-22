from notes_api.app import app
from notes_api.routes.note import router as NoteRouter


@app.get("/", tags=["Root"])
def root():
    return {"message": "Welcome to my Notes API"}


app.include_router(NoteRouter)
