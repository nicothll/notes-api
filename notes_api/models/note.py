from beanie import Document


class Note(Document):
    title: str
    description: str
    checked: bool = False

    class Settings:
        name = "notes"
