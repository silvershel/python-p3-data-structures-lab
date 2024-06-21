spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = []
    for food in spicy_foods:
        names.append(food["name"])
    return names

def get_spiciest_foods(spicy_foods):
    dictionary = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            dictionary.append(food)
    return dictionary

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        food_string = food["name"] + " (" + food["cuisine"] + ") | Heat Level: " + "🌶" * food["heat_level"]
        print(food_string)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    food_dict = {}
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            food_dict = food
            break
        # break stops the code from running returning the first instance of the cuisine found
    return food_dict

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        food_string = food["name"] + " (" + food["cuisine"] + ") | Heat Level: " + "🌶" * food["heat_level"]
        if food["heat_level"] > 5:
            print(food_string)


def get_average_heat_level(spicy_foods):
    heat_levels = []
    for food in spicy_foods:
        heat_levels.append(food["heat_level"])
    return sum(heat_levels) / len(heat_levels)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return(spicy_foods)
