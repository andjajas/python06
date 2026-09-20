import alchemy

print(alchemy.create_air())

try:
    alchemy.create_earth()
except AttributeError:
    print("mudule 'alchemy' has no attribute 'create_earth")
