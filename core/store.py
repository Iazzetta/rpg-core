from typing import List
from pydantic import BaseModel, Field
from core.item import Item
from core.player import Player
from core.constants import ITEM_PRICE_DEVALUATION


class Store(BaseModel):
    items: List[Item] = Field(default=[])

    def add_item(self, item: Item):
        self.items.append(item)

    def get_item(self, item_id: int):
        try:
            selected_item = list(filter(lambda i: i.id == item_id, self.items))[0]
            return selected_item
        except:
            print("Item não encontrado")

        return False

    def buy_item(self, buyer: Player, item_id: int):
        selected_item = self.get_item(item_id)

        default_price = selected_item.price

        discount = buyer.persuasion_discount()

        if discount > 0:
            print("Você conseguiu um desconto na compra do item!")
            default_price -= discount

        if buyer.coins < default_price:
            print(f"Você não tem saldo para comprar o item {selected_item.name}")
            return

        buyer.coins -= default_price

        buyer.inventory.add(selected_item)
        print(f"Você comprou o item {selected_item.name}")

    def sell_item(self, seller: Player, item_id: int):
        selected_item = self.get_item(item_id)

        if not seller.inventory.get_item(item_id):
            return

        seller.inventory.rem(selected_item)

        price_decrement = selected_item.price * (ITEM_PRICE_DEVALUATION / 100)
        final_price = selected_item.price - price_decrement

        seller.coins += final_price
