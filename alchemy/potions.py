from .elements import create_air, create_earth
from elements import create_water, create_fire


def strength_potion() -> str:
    return (
        f"Strength potion brewed with "
        f"’{create_fire()}’ and ’{create_water()}”"
    )


def healing_potion() -> str:
    return (
        f"Healing potion brewed with "
        f"’{create_earth()}’ and ’{create_air()}”"
    )
