from typing import Optional
from pydantic import BaseModel
from beanie import Document


class Category(BaseModel):
    name: str
    description: Optional[str]

    class Settings:
        name = "categories"


class Note(Document):
    title: str
    description: str
    checked: bool
    category: Optional[Category]

    class Settings:
        name = "notes"
