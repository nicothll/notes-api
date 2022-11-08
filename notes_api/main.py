from .app import app
from .routes.note import router as NoteRouter


@app.get("/", tags=["Root"])
def root():
    return {"message": "Welcome to my Notes API"}


app.include_router(NoteRouter)
