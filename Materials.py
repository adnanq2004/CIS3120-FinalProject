from Items import Items

class Materials(Items):
    def __init__(self, location, identifier, category, flavortext, name, effect, hearts):
        super().__init__(location, identifier, category, flavortext, name)
        
        self._effect = effect
        self._hearts = hearts
        
        
    def give_effect(self):
        return self._effect
    
    def give_hearts(self):
        return self._hearts
    
    def compare_hearts(self, other):
        if self.give_hearts() > other.give_hearts():
            return self
        elif self.give_hearts() < other.give_hearts():
            return other
        else:
            return 0
        
    