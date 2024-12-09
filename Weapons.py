From Items import Items

class Weapons(Items):
    def __init__(self, location, identifier, categorgy, flavortext, damage, defense, durability):
        super().__init__(self, location, identifier, categorgy, flavortext)
        
        # damage, which should give the base amount of damage
        # defense, which should give the base amount of defense
        # duraility, which should give the base amount of max durability
        
        self._damage=damage
        self._defense=defense
        self._durability=durability
        
    def give_damage(self):
        return self._damage
    
    def give_defense(self):
        return self._defense
    
    def give_durability(self):
        return self._durability