def read_recipe(path: str) -> dict | None:
    import json
    try:
        with open(path, "r") as file:
                return json.load(file)
    except:
         return None

def read_recipes(directory_path: str) -> list:
    from os import listdir
    recipes = []
    for recipe_file in listdir(directory_path):
        recipe = read_recipe(directory_path + recipe_file)
        recipes.append(recipe)
    return recipes

def calculate_probabilities(recipes: list) -> dict:
    from datetime import date
    probabilities = {}
     
    today = date.today()
    for recipe in recipes:
        time_diff = abs(date.fromisoformat(recipe["Last Made"]) - today)
        
        probability = recipe["Average Rating"]
        if time_diff.days < 10:
            probability = probability - 5
            if probability < 0:
                 probability = 0
        else:
             probability = probability + (time_diff.days() * 0.5)
        
        probabilities[recipe["Name"]] = probability
    
    # Normalize
    total = float(sum(probabilities.values()))
    for key, value in probabilities.items():
            probabilities[key] = value / total
    
    return probabilities

def random_recipe(normalized_probabilities: dict) -> dict:
    import random
    rand = random.random()

    threshold = 0.0
    for key in normalized_probabilities.keys():
        value = normalized_probabilities[key]

        if value == 0:
            continue

        threshold = threshold + value

        if rand < threshold:
            return key


if __name__ == "__main__":
    recipes = read_recipes("./recipes/")
    probabilities = calculate_probabilities(recipes)
    recipe = random_recipe(probabilities)
    print(recipe)