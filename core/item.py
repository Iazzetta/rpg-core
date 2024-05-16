from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field
from core.attribute import Attribute


class WeaponType(str, Enum):
    MELEE = "melee"  # arma branca (adaga, espada, machado)
    RANGED = "ranged"  # arma de longo alcance (arco e flecha)
    MAGIC = "magic"  # arma magica (cajado)


class ItemType(str, Enum):
    WEAPON = "weapon"
    HEAD = "head"
    BODY = "body"
    HAND = "hand"
    FEET = "feet"
    HP_POTION = "hp_potion"


class Item(Attribute):
    id: int
    name: str
    item_type: ItemType
    weapon_type: Optional[WeaponType] = Field(default=None)
    price: float = Field(default=0.0)
