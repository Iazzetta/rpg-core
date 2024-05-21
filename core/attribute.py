from pydantic import BaseModel, Field


class Attribute(BaseModel):
    intelligence: float = Field(default=0)  # + magic dmg
    constitution: float = Field(default=0)  # + hp
    dexterity: float = Field(default=0)  # + dano arma longo alcance (arqueiro)
    strength: float = Field(default=0)  # + dano arma branca
    persuasion: float = Field(default=0)  # % de chance de aplicar um desconto na compra
    speed_attack: float = Field(default=0)  # velocidade de ataque
    critical: float = Field(default=0)  # % de chance de duplicar o dano
    magic_defense: float = Field(default=0)
    physical_defense: float = Field(default=0)
