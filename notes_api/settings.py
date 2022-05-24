import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()


class Settings(BaseModel):
    mongo_uri = os.getenv("MONGODB_LOCAL")


CONFIG = Settings()
