# CIS3120-FinalProject

Video Presentation: https://youtu.be/LszoxwwYh0A

## What is this project?

In this project, I performed various analytics on data I gathered from an API called "Hyrule-Compendium-API". https://github.com/gadhagod/Hyrule-Compendium-API

I made use of Python libraries such as Pandas and Matplotlib to perform analytical operations on data, as well as Object Oriented Programming to create parent and child classes to better manipulate data.

## How to use:

This Project does not require an API Key. 

To use it, run the file "Project.py" through Python, for example on terminal. You'll be given a prompt to input a value, along with instructions on what to input. Following the instructions leads to a few specific instances of analytics I performed on the data.

The first selection will require an input within the range 1-3, leading to accessing a different dataset from the API, Weapons, Food, and Materials.

If 1 is selected, the program will lead to a selection of analytics for the Weapons appropriate data. The user will then have to select an input within the range 1-6. 1 will find the Weapon with the highest damage stat, 2 will find the Shield with the highest defense stat, 3 will pick 2 random Weapons and find the stronger of the two, 4 will sum the number of occurences of Weapons for every location, and then graph the 5 highest values in a pie chart with numerical labels of their percentages, 5 will find the average damage of all Weapons in every location and graph the 10 highest values in a bar graph, 6 will find the average defense of all Shields in every location and graph the 10 highest values in a bar graph.

If 2 is selected, the program will lead to a selection of analytics for the Food appropriate data. The user will then have to select an input within the range 1-5. 1 will find the Food with the highest raw healing effect, 2 will select a random Food item and give information about it, 3 will generate a list of all buffs and let the user select one then view all Food items with that effect, 4 will sum the number of occurences of Food for every location, and then graph the 5 highest values in a pie chart with numerical labels of their percentages, 5 will find the average healing effect of all Food in every location and graph the 10 highest values in a bar graph.

If 3 is selected, the program will lead to a selection of analytics for the Materials appropriate data. The user will then have to select an input within the range 1-5. 1 will find the Materials with the highest raw healing effect, 2 will select a random Materials item and give information about it, 3 will generate a list of all buffs and let the user select one then view all Materials items with that effect, 4 will sum the number of occurences of Materials for every location, and then graph the 5 highest values in a pie chart with numerical labels of their percentages, 5 will find the average healing effect of all Materials in every location and graph the 10 highest values in a bar graph.
