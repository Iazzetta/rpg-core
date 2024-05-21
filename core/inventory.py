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
        if len(self.items) < self.max_size:
            self.items.append(item)
            print(f"Item '{item.name}' adicionado ao inventário")
        else:
            print(f"O inventário está cheio. Não foi possível adicionar {item.name}")

    def rem(self, item: Item):
        if item in self.items:
            self.items.remove(item)
            print(f"Item '{item.name}' removido ao inventário")
        else:
            print("O item especificado não está no inventário")

    def get_item(self, item_id: int):
        try:
            selected_item = list(filter(lambda i: i.id == item_id, self.items))[0]
            return selected_item
        except:
            print("Item não encontrado no inventário")
        return False
