from Items import Items

class Materials(Items):
    def __init__(self, location, identifier, category, flavortext, ):
        super().__init__(location, identifier, category, flavortext)
        
        # 