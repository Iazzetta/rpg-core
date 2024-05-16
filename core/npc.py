from pydantic import BaseModel


class NPC(BaseModel):
    name: str
    description: str
