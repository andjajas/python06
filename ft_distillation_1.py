#!/usr/bin/env python3
import alchemy
from alchemy import healing_potion as heal

print("=== Distillation 1 ===")
print("Using: 'import alchemy' structure to access potions")
print(f"Testing strength_potion: {alchemy.strength_potion()}")
print(f"Testing heal alias: {heal()}")
