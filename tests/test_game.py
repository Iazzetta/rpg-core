from core.player import Player
from core.inventory import Inventory
from core.store import Store
from core.merchant import Merchant
from core.item import Item, WeaponType, ItemType
import time

# criando o player
player = Player(id=1, name="ppy")

# definindo os atributos do player
player.upgrade_attribute("critical")
player.upgrade_attribute("critical")
player.upgrade_attribute("critical")
player.upgrade_attribute("critical")
player.upgrade_attribute("strength")

# criando uma loja
store = Store()

# criando os itens
adaguinha = Item(
    id=1,
    name="adaga",
    item_type=ItemType.WEAPON,
    weapon_type=WeaponType.MELEE,
    strength=5,
    price=10,
)

espada_madeira = Item(
    id=2,
    name="Espada de Madeira",
    item_type=ItemType.WEAPON,
    weapon_type=WeaponType.MELEE,
    strength=20,
    price=150,
)

store.add_item(adaguinha)
store.add_item(espada_madeira)

merchant = Merchant(
    name="Jairo", description="Venha comprar umas espadinhas comigo", store=store
)

merchant.welcome()

# comprar o item adaguinha
merchant.store.buy_item(buyer=player, item_id=1)

# equipando a adaga
player.use_item(adaguinha)

# calculando ataque basico
player.basic_damage_attack()
