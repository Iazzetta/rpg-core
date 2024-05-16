from typing import List
from pydantic import BaseModel, Field
from core.item import Item
from core.player import Player


class Store(BaseModel):
    items: List[Item] = Field(default=[])

    def add_item(self, item: Item):
        self.items.append(item)

    def buy_item(self, buyer: Player, item_id: int):
        selected_item = None

        for item in self.items:
            if item.id == item_id:
                selected_item = item

        if not selected_item:
            print("Item não encontrado")
            return

        if buyer.coins < selected_item.price:
            print(f"Você não tem saldo para comprar o item {selected_item.name}")
            return

        buyer.coins -= selected_item.price

        buyer.inventory.add(selected_item)
        print(f"Você comprou o item {selected_item.name}")
