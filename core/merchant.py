from pydantic import Field
from core.npc import NPC
from core.store import Store


class Merchant(NPC):
    store: Store = Field(default=None)

    def welcome(self):
        print(f"[{self.name}] {self.description}")
