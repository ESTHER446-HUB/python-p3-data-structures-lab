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
    """Return a list of the names of all spicy foods."""
    return [food["name"] for food in spicy_foods]


def get_spiciest_foods(spicy_foods):
    """Return a list of foods with heat_level greater than 5."""
    return [food for food in spicy_foods if food["heat_level"] > 5]


def print_spicy_foods(spicy_foods):
    """Print each food in the format: Name (Cuisine) | Heat Level: 🌶 emojis."""
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat = "🌶" * food["heat_level"]
        print(f"{name} ({cuisine}) | Heat Level: {heat}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """Return the first food dictionary that matches the given cuisine."""
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food


def print_spiciest_foods(spicy_foods):
    """Print only foods with heat_level greater than 5 in the same format."""
    for food in spicy_foods:
        if food["heat_level"] > 5:
            name = food["name"]
            cuisine = food["cuisine"]
            heat = "🌶" * food["heat_level"]
            print(f"{name} ({cuisine}) | Heat Level: {heat}")


def get_average_heat_level(spicy_foods):
    """Return the average heat level of all foods."""
    total = sum(food["heat_level"] for food in spicy_foods)
    return total / len(spicy_foods)


def create_spicy_food(spicy_foods, spicy_food):
    """Return a new list with the new spicy food added."""
    return spicy_foods + [spicy_food]
