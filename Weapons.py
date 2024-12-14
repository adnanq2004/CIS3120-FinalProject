from Items import Items

class Weapons(Items):
    def __init__(self, location, identifier, category, flavortext, damage, defense):
        super().__init__(location, identifier, category, flavortext)
        
        # damage, which should give the base amount of damage
        # defense, which should give the base amount of defense
        
        self._damage=damage
        self._defense=defense
        
    def give_damage(self):
        return self._damage
    
    def give_defense(self):
        return self._defense