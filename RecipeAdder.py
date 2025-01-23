import json, statistics, datetime, re

def add_recipe() -> None:
    cont = True
    while(cont):
        print("Adding a recipe:")
        
        name = input("\tRecipe Name: ")
        
        location = input("\tRecipe Location: ")
        
        lastmade = input("\tDay last made (YYYY-MM-DD or press enter for today's date): ")
        if lastmade == "":
            lastmade = datetime.date.today().isoformat()
        
        ratings = []
        i = 1
        rating = input(f"\tRating {i}: ")
        while rating.isdigit():
            ratings.append(int(rating))
            i = i + 1
            rating = input(f"\tRating {i}: ")
        
        save_recipe(name, location, lastmade, ratings)
        print("Recipe Added")
        
        cont_ans = input("\nContinue? (y/n): ")
        print()
        if cont_ans != "y":
            cont = False

def save_recipe(name: str, location: str, lastmade: str, ratings) -> None:
    recipe = {
        "Name": name,
        "Location": location,
        "Last Made": lastmade,
        "Average Rating": statistics.mean(ratings)
    }

    file_name = "./recipes/" + re.sub('[^A-Za-z0-9]+', '', name) + ".json"
    
    try:
        with open(file_name, "x") as file:
            file.write(json.dumps(recipe))
    except:
        cont_ans = input("File already exists. Overwrite? (y/n): ")
        if cont_ans != "y":
            return

        with open(file_name, "w") as file:
                file.write(json.dumps(recipe))


if __name__ == "__main__":
    add_recipe()