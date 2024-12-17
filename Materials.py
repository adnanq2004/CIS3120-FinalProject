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
            return self
        
    def compare_many(self, list_mates):
        
        the_strongest=list_mates[0]
        
        
        for i in list_mates:
            the_strongest=the_strongest.compare_hearts(i)
            
        return the_strongest
    
    def give_info(self):
        print(f"Great! This material item is {self.give_name()}, which heals {self.give_hearts()} hearts and has the effect {self.give_effect()}")