from ..elements import create_air
from elements import create_fire
from ..potions import strength_potion

def lead_to_gold() -> str:
    return f"Recipe transmuting Lead to Gold: brew ’[created air]’" \
    f"and ’[created strength potion]’ mixed with ’[created fire]’"