import json, statistics

numPeople = 5
    
def readRecipes(fileloc: str) -> dict:
    try:
        with open(fileloc, "r") as file:
           return json.load(file)
    except:
        return {}
    
def writeRecipes(fileloc: str, recipes: dict) -> None:
    with open(fileloc, "w") as file:
        file.write(json.dumps(recipes))

recipes = readRecipes("recipes.json")

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
        print()
        if cont_ans != "y":
            cont = False


def saveRecipe(name: str, location: str, ratings: list[float]) -> None:
    recipes[name] = {
        "Location": location,
        "Rating": statistics.mean(ratings),
    }


if __name__ == "__main__":
    addRecipe()
    writeRecipes("recipes.json", recipes)