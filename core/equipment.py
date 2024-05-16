from typing import Optional
from pydantic import BaseModel, Field
from core.item import Item


class Equipment(BaseModel):
    head: Optional[Item] = Field(default=None)
    body: Optional[Item] = Field(default=None)
    hand: Optional[Item] = Field(default=None)
    feet: Optional[Item] = Field(default=None)
    weapon: Optional[Item] = Field(default=None)
