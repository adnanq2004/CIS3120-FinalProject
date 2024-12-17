from Items import Items

class Weapons(Items):
    def __init__(self, location, identifier, category, flavortext, name, damage, defense):
        super().__init__(location, identifier, category, flavortext, name)
        
        # damage, which should give the base amount of damage
        # defense, which should give the base amount of defense
        
        # hopefully, this can get rid of the issue with arrows
        
        
        if (damage == None):
            self._damage=0
        else:
            self._damage=damage
        if (defense == None):
            self._defense=0
        else:
            self._defense=defense
        
    def give_damage(self):
        return self._damage
    
    def give_defense(self):
        return self._defense
    
    # will now many functions to do some analysis, generally will be simple things, like comparing the damage of two weapons
    # or comparing damage and defense, and saying the two can't be compared because one is a weapon and one is a shield
    
    def compare(self, other):
        # check if one is an arrow
        if (self.give_defense == None or self.give_damage == None):
            return other
        if (other.give_defense == None or other.give_damage == None):
            return self
        
        
        # check if both are shields
        if (self.give_defense() == 0 and other.give_defense() == 0):
            if (self.give_damage()>other.give_damage()):
                return self
            elif (self.give_damage()<other.give_damage()):
                return other
            else:
                return self
        
        # check if both are shields
        if (self.give_damage() == 0 and other.give_damage() == 0):
            if (self.give_defense()>other.give_defense()):
                return self
            elif (self.give_defense()<other.give_defense()):
                return other
            else:
                return self
            
        return 0
        
        # by having it return the variable itself that has the higher stats, will be faster to use
        # also, didn't program any fail safe if they are not the same weapon type, will trust human capability for now
    
    def compare_many(self, list_weapons):
        
        # again, no failsafe if any element in list_weapons is not the same type as self. idk what to do until that situation happens
        
        # temporarily setting self as strongest
        
        # warning about use case:
        # generally should be like: list_weapons[0].compare_many(list_weapons)
        
        the_strongest=list_weapons[0]
        for i in range(1,len(list_weapons)+1):
            # for some reason, this is producing an int object instead of a Weapons object when the one-hit-obliterator is compared to an arrow
            # ????
            print("=======", list_weapons[i].give_damage())
            the_strongest = the_strongest.compare(list_weapons[i])
            print(i, the_strongest)
            print(i, the_strongest.give_name())
        
        return the_strongest
        
#         for i in list_weapons:
#             the_strongest=the_strongest.compare(i)
#             print(the_strongest.give_name())
            
#         return the_strongest
    
    