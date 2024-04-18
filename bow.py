from collections.abc import Iterable


class MinecraftBow:
    # Damage
    # Durability
    # Crafting Materials
    # Enchantments
    # Name
    #ID 
    def __init__(self):
        self.damage = 3
        self.durability = 400
        self.enchantments = []
        self.name = "Bow"
        
    def changeName(self, newName):
        self.name = newName
        
    
        
    
bow1 = MinecraftBow()
print(bow1.name)