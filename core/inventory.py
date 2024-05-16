from typing import List
from pydantic import BaseModel, Field
from core.item import Item, ItemType


class Inventory(BaseModel):
    items: List[Item] = Field(default=[])
    max_size: int = Field(default=15)

    def is_equippable(self, item: Item):
        return item.item_type in [
            ItemType.WEAPON,
            ItemType.HEAD,
            ItemType.BODY,
            ItemType.HAND,
            ItemType.FEET,
        ]

    def add(self, item: Item):
        self.items.append(item)
        print(f"Item '{item.name}' adicionado ao inventário")

    def rem(self, item: Item):
        for i, _ in enumerate(self.items):
            if _ == item:
                del self.items[i]
        print(f"Item '{item.name}' removido ao inventário")
