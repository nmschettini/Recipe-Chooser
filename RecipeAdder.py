import json, statistics,re

numPeople = 5

def addRecipe():
    cont = True
    while(cont):
        print("Adding a recipe:")
        
        name = input("\tRecipe Name: ")
        location = input("\tRecipe URL (or location): ")
        ratings = []
        for i in range(numPeople):
            ratings.append(int(input(f"\tRating {i+1}: ")))
        saveRecipe(name, location, ratings)
        
        print("Recipe Added")
        
        cont_ans = input("\nContinue? (y/n): ")
        if cont_ans != "y":
            cont = False


def saveRecipe(name: str, location: str, ratings: list[float]) -> None:
    recipe = {
        "Name": name,
        "Location": location,
        "Rating": statistics.mean(ratings)
    }

    recipe_json = json.dumps(recipe)

    with open(f"./Recipes/{re.sub('[^A-Za-z0-9]+', '', name)}.json", "w") as file:
        file.write(recipe_json)


if __name__ == "__main__":
    addRecipe()