#from API_key import api_key
import requests
import pandas as pd

from matplotlib import pyplot as plt

from Items import Items
from Materials import Materials
from Food import Food
from Weapons import Weapons

# ================================================================================

# test functionality of classes

thing = Items("plateu", "123", "None", "this is a test")
thing.give_location()



# will open API and scope out some info

url="https://botw-compendium.herokuapp.com/api/v3/compendium/all"

response = requests.get(url)

# print(response.status_code)
# response code 200, all is well

# this doesn't work because the "all is too big"
# print(response.json)

data = response.json()

print(data.get("data")[0].get("category"))

# IT WORKS



# something