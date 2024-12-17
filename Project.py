#from API_key import api_key
import requests
import pandas as pd

from matplotlib import pyplot as plt

import statistics
import random

from Items import Items
from Weapons import Weapons
from Materials import Materials
from Food import Food

# ================================================================================

# will open API and scope out some info

url="https://botw-compendium.herokuapp.com/api/v3/compendium/all"

response = requests.get(url)

# print(response.status_code)
# response code 200, all is well

# this doesn't work because the "all is too big"
# print(response.json)

data = response.json()


if "data" in data:
    all_df=pd.DataFrame.from_dict(data["data"])
else:
    print("error in getting data")

# all_df
# IT WORKS



# will make dataframes for equipment, food, and materials

equip_df=all_df[all_df["category"]=="equipment"]
food_df=all_df[all_df["category"]=="materials"]
materials_df=all_df[all_df["edible"]==True]


# time to turn damage and defense, that are normally stored in properties column, into their own column


damage_list = []
defense_list = []

for i in range(equip_df.shape[0]):
    damage_list.append(equip_df["properties"].iloc[i].get("attack"))
    defense_list.append(equip_df["properties"].iloc[i].get("defense"))
    
equip_df = equip_df.drop(labels="properties", axis=1)
equip_df=equip_df.assign(damage=damage_list)
equip_df=equip_df.assign(defense=defense_list)



# the functions to convert dataframe info into a list of Weapons, Materials, and Food objects

def df_to_weap_list(equip_df):
    column_names = []
    final_list = []
    
    for i in equip_df:
        # print(i)
        column_names.append(i)
        
    for i in range(equip_df.shape[0]):
        temp_weapon = Weapons(location=equip_df["common_locations"].iloc[i],identifier=equip_df["id"].iloc[i],category="weapon",flavortext=equip_df["description"].iloc[i],name=equip_df["name"].iloc[i],damage=equip_df["damage"].iloc[i],defense=equip_df["defense"].iloc[i])
        final_list.append(temp_weapon)
        
    return final_list


def df_to_mate_list(materials_dfs):
    column_names = []
    final_list = []
    
    for i in materials_dfs:
        # print(i)
        column_names.append(i)
        
    for i in range(materials_dfs.shape[0]):
        temp_material = Materials(location=materials_dfs["common_locations"].iloc[i],identifier=materials_dfs["id"].iloc[i],category="material",flavortext=materials_dfs["description"].iloc[i],name=materials_dfs["name"].iloc[i],effect=materials_dfs["cooking_effect"].iloc[i],hearts=materials_dfs["hearts_recovered"].iloc[i])
        final_list.append(temp_material)
        
    return final_list


def df_to_food_list(food_df):
    column_names = []
    final_list = []
    
    for i in food_df:
        # print(i)
        column_names.append(i)
        
    for i in range(food_df.shape[0]):
        temp_food = Food(location=food_df["common_locations"].iloc[i],identifier=food_df["id"].iloc[i],category="food",flavortext=food_df["description"].iloc[i],name=food_df["name"].iloc[i],effect=food_df["cooking_effect"].iloc[i],hearts=food_df["hearts_recovered"].iloc[i])
        final_list.append(temp_food)
        
    return final_list



# first graphic analysis
# will happen after user selects: weapons, and then eventually display most common locations
# will take input: dataframe of Weapons class objects, no filter
# will give output: display pie chart, each wheel should be a location

# how the code should work: 
# iterate through dataframe of Weapons, make a dictionary of each location, with a tally of encounters
# make pie chart

# decided to broaden it to be applicable to all three dataframes


# will probably follow this format for subsequent analysis functions
def locations_compare(the_df):
    dict_loc = {}
    
    # check if item in location exists in dictionary, if not add it. add a tally
    for i in the_df["common_locations"]:
        # print(i)
        if (i is not None):
            for j in i:
                if j in dict_loc:
                    dict_loc[j]+=1
                else:
                    dict_loc[j]=1
    
    # what if i make this fucntion return the dictionary with the data, and then have a separate function to display the chart
    return dict_loc

# this function will graph the data
# input: a dictionary with the common locations, with a value tally next to it
def graph_locations_compare(dict_loc, tit):
    # might only show the top 5
    temp_dict_loc=dict(sorted(dict_loc.items(), key=lambda item: item[1]))
    
    labels={key: value for key, value in sorted(dict_loc.items(), key=lambda item: item[1], reverse=True)[:5:]}.keys()
    sizes=[]
    for i in labels:
        sizes.append(dict_loc[i])
    
    plt.pie(sizes, labels=labels, autopct='%.2f')
    plt.title(tit)
    
    plt.show()


# new function to select a random item, twice, and then compare them

# assume input list of object
def random_select(the_list):
    return the_list[random.randint(0,len(the_list)+1)]

def random_weapons():
    weap_list = df_to_weap_list(equip_df[equip_df["defense"] == 0])
    weap_1 = random_select(weap_list)
    weap_2 = random_select(weap_list)
    print(f"the two random weapons are: {weap_1.give_name()} with a damage stat of {weap_1.give_damage()} vs {weap_2.give_name()} with a damage stat of {weap_2.give_damage()}.")
    print(f"the stronger weapon is: {weap_1.compare(weap_2).give_name()}!!")

def random_mate_food(the_df):
    # assume input is material df or food df
    sort_list = df_to_mate_list(the_df)
    item_1 = random_select(sort_list)
    item_1.give_info()
    
# new function to find average damage or defense per location

def average_dam_loc(the_df,stat):
    # take input: weapons dataframe that's filtered with defense=0 or damage=0
    # the value of stat must be either "damage" or "defense"
    # gives output: output for groupby, will figure out how to display graphically as well
    
    # this should split it into the different possible locations, and then find average
    # this is more complicated than i initially thought, i just realized, because common_locations is a list
    # meaning just using the groupby method will probably not work
    
    the_stats = {}
    
    for i in range(the_df.shape[0]):
        if (the_df["common_locations"].iloc[i] is not None):
            for j in the_df["common_locations"].iloc[i]:
                # print(j)
                if j not in the_stats:
                    the_stats[j]=[]
                the_stats[j].append(the_df[stat].iloc[i])
                
                
    for i in the_stats:
        the_stats[i] = statistics.mean(the_stats[i])
 
    # only show the top 10
    the_stats={key: value for key, value in sorted(the_stats.items(), key=lambda item: item[1], reverse=True)[:10:]}
    
    
    # will make a histogram/bar graph
    
    temp_series = pd.Series(the_stats)
    
    temp_series.plot(kind="bar")
    
    plt.title("Highest Average in Locations")
    plt.xlabel("Location")
    plt.ylabel(stat)
    
    plt.show()
    

# this function will handle requiring user inputs to help user navigate through different analyitic outputs

def main_user_relations():
    
    print("="*100)
    
    print("Hello, welcome to my Project! Please type one of the following to navigate further in:")
    print("1: To deal with Weapons")
    print("2: To deal with Food")
    print("3: To deal with Materials")
    
    usr_input=0
    while (usr_input==0):
        usr_input = int(input("Please input your number here: "))
        
        # dealing with weapons
        if usr_input == 1:
            print("="*100)
            print("Hello, please select one of the following options:")
            print("1: Find the strongest weapon in BOTW")
            print("2: Find the strongest shield in BOTW")
            print("3: Compare two random weapons in BOTW")
            print("4: Find the highest variety of weapons in locations in BOTW")
            print("5: Find the average damage of weapons in locations in BOTW")
            print("6: Find the average defense of weapons in locations in BOTW")
            usr_input = 0
            while usr_input == 0:
                usr_input = int(input("Please input your number here: "))
                if usr_input == 1:
                    stored = df_to_weap_list(equip_df[equip_df["defense"]==0])
                    the_weapon = stored[0].compare_many(stored)
                    print(f"Great! The strongest weapon is {the_weapon.give_name()}, with a damage stat of {the_weapon.give_damage()}")
                elif usr_input == 2:
                    stored = df_to_weap_list(equip_df[equip_df["damage"]==0])
                    the_weapon = stored[0].compare_many(stored)
                    print(f"Great! The strongest shield is {the_weapon.give_name()}, with a defense stat of {the_weapon.give_defense()}")    
                elif usr_input == 3:
                    random_weapons()
                elif usr_input == 4:
                    graph_locations_compare(locations_compare(equip_df[equip_df["defense"]==0]), "Weapons")
                    # debating whether to go into more deail about actual results or if just displaying the graph is enough    
                elif usr_input == 5:
                    average_dam_loc(equip_df[(equip_df["defense"]==0)],"damage")
                elif usr_input == 6:
                    average_dam_loc(equip_df[(equip_df["damage"]==0)],"defense")
                else:
                    print("That's not a valid answer! Please try again.")
                    usr_input=0
                
        # dealing with food
        elif usr_input == 2:
            print("="*100)
            print("Hello, please select one of the following options:")
            print("1: Find the most healing food in BOTW")
            print("2: Get Information about a random food in BOTW")
            print("3: View all food items for a given buff")
            print("4: Find the highest variety of food in locations in BOTW")
            print("5: Find the average healing of food in locations in BOTW")
            usr_input = 0
            while usr_input == 0:
                usr_input = int(input("Please input your number here: "))
                if usr_input == 1:
                    stored = df_to_food_list(food_df)
                    the_food = stored[0].compare_many(stored)
                    the_food.give_info()
                elif usr_input == 2:
                    random_mate_food(food_df)
                elif usr_input == 3:
                    print("="*100)
                    # make a list of all buffs
                    list_buffs = food_df["cooking_effect"].unique()
                    usr_input = 0
                    while (usr_input == 0):
                        usr_input = int(input(f"Please pick a number between 0 and {len(list_buffs)}"))
                        if usr_input not in range(0, len(list_buffs)):
                            print("Please try again.")
                            usr_input = 0
                        else:
                            list_buffs = df_to_food_list(food_df[food_df["cooking_effect"]==list_buffs[usr_input]])
                            for i in list_buffs:
                                i.give_info()
                elif usr_input == 4:
                    graph_locations_compare(locations_compare(food_df), "Unique Food Items")
                elif usr_input == 5:
                    average_dam_loc(food_df,"hearts_recovered")
                else:
                    print("That's not a valid answer! Please try again.")
                    usr_input=0
            
        # dealing with materials
        elif usr_input == 3:
            print("="*100)
            print("Hello, please select one of the following options:")
            print("1: Find the most healing material in BOTW")
            print("2: Get Information about a random material in BOTW")
            print("3: View all material items for a given buff")
            print("4: Find the highest variety of material in locations in BOTW")
            print("5: Find the average healing of material in locations in BOTW")
            usr_input = 0
            while usr_input == 0:
                usr_input = int(input("Please input your number here: "))
                if usr_input == 1:
                    stored = df_to_food_list(materials_df)
                    the_food = stored[0].compare_many(stored)
                    the_food.give_info()
                elif usr_input == 2:
                    random_mate_food(materials_df)
                elif usr_input == 3:
                    print("="*100)
                    # make a list of all buffs
                    list_buffs = materials_df["cooking_effect"].unique()
                    usr_input = 0
                    while (usr_input == 0):
                        usr_input = int(input(f"Please pick a number between 0 and {len(list_buffs)}"))
                        if usr_input not in range(0, len(list_buffs)):
                            print("Please try again.")
                            usr_input = 0
                        else:
                            list_buffs = df_to_mate_list(materials_df[materials_df["cooking_effect"]==list_buffs[usr_input]])
                            for i in list_buffs:
                                i.give_info()
                elif usr_input == 4:
                    graph_locations_compare(locations_compare(materials_df), "Unique Food Items")
                elif usr_input == 5:
                    average_dam_loc(materials_df,"hearts_recovered")
                else:
                    print("That's not a valid answer! Please try again.")
                    usr_input=0
        
        else:
            print("That's not a valid answer! Please try again.")
            usr_input=0
                
    
    print("="*100)
    
main_user_relations()