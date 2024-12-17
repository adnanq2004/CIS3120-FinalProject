class Items:
    def __init__(self, location, identifier, category, flavortext, name):
        # items need to have the following variables:
        # locations, which should list places they are commonly found
        # id, which should give in game id
        # category, which should give the distinction of being a weapon, material, etc. will use this to split data into childs
        # description, which should give in game flavor text
        
        #normally, I wouldn't add the underscore before the variables, but will do so now, because good practice.
        if (location == None):
            self._location = []
        else:
            self._location = location
        self._id = identifier
        self._category = category
        self._description = flavortext
        self._name = name
        
        
    # will make various functions to return the class's variables
    
    def give_location(self):
        # initially, will just return the array of locations as it is
        # eventually, might make it print the details
        return self._location
    
    def give_id(self):
        return self._id
    
    def give_category(self):
        return self._category
    
    def give_description(self):
        return self._description
    
    def give_name(self):
        return self._name
    
    
    def compare_many(self, list_mates):
        
        the_strongest=list_mates[0]
        
        
        for i in list_mates:
            the_strongest=the_strongest.compare_hearts(i)
            
        return the_strongest
    
    def give_info(self):
        print(f"Great! This food item is {the_food.give_name()}, which heals {the_food.give_hearts()} hearts and has the effect {the_food.give_effect()}")