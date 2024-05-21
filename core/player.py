from random import randint
from pydantic import BaseModel, Field
from core.attribute import Attribute
from core.equipment import Equipment
from core.item import Item, WeaponType
from core.inventory import Inventory

from core.constants import (
    CRITICAL_TOTAL_PERCENT,
    CRITICAL_MULTIPLIER,
    CRITICAL_INITIAL_PERCENT,
    ATTRIBUTE_INCREMENT,
    PERSUASION_TOTAL_PERCENT,
    PERSUASION_INITIAL_PERCENT,
    PERSUASION_DISCOUNT,
    PERSUASION_MULTIPLIER,
)


class Player(BaseModel):
    id: int
    name: str
    hp: int = Field(default=100)
    hp_max: int = Field(default=100)
    mana: int = Field(default=50)
    mana_max: int = Field(default=50)
    exp: float = Field(default=100)
    exp_max: float = Field(default=100)
    coins: float = Field(default=100)
    level: int = Field(default=1)
    attribute_points: int = Field(default=5)
    attributes: Attribute = Field(default=Attribute())
    equipment: Equipment = Field(default=Equipment())
    inventory: Inventory = Field(default=Inventory())

    def upgrade_attribute(self, attribute_type: str):
        if self.attribute_points > 0:
            setattr(
                self.attributes,
                attribute_type,
                getattr(self.attributes, attribute_type) + ATTRIBUTE_INCREMENT,
            )
            self.attribute_points -= 1
        else:
            print("você não tem pontos de atributo")

    def use_item(self, item: Item):
        if item not in self.inventory.items:
            print("Você não possui esse item no inventário")
            return

        if self.inventory.is_equippable(item):
            old_item = getattr(self.equipment, item.item_type.value)
            if old_item:
                self.inventory.add(old_item)
            setattr(self.equipment, item.item_type.value, item)
            self.inventory.rem(item)
            print(f"Item {item.name} adicionado ao equipamento")

    def persuasion_discount(self):
        discount = 0
        total_persuasion = self.attributes.persuasion

        if self.equipment.weapon:
            total_persuasion += self.equipment.weapon.persuasion

        rand_persuasion_chance = randint(
            PERSUASION_INITIAL_PERCENT, PERSUASION_TOTAL_PERCENT
        )
        total_persuasion *= PERSUASION_MULTIPLIER

        if rand_persuasion_chance <= total_persuasion:
            discount = PERSUASION_DISCOUNT

        return discount

    def basic_damage_attack(self):
        damage = 0

        # weapon attributes
        if self.equipment.weapon:
            if self.equipment.weapon.weapon_type == WeaponType.MELEE:
                damage += self.attributes.strength + self.equipment.weapon.strength
            if self.equipment.weapon.weapon_type == WeaponType.MAGIC:
                damage += (
                    self.attributes.intelligence + self.equipment.weapon.intelligence
                )
            if self.equipment.weapon.weapon_type == WeaponType.RANGED:
                damage += self.attributes.dexterity + self.equipment.weapon.dexterity

        # critical calc
        total_critical = self.attributes.critical
        if self.equipment.weapon:
            total_critical += self.equipment.weapon.critical

        rand_critical_chance = randint(CRITICAL_INITIAL_PERCENT, CRITICAL_TOTAL_PERCENT)
        if rand_critical_chance <= total_critical:
            damage *= CRITICAL_MULTIPLIER

        return damage
