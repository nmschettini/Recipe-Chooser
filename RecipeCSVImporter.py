from RecipeAdder import save_recipe
import pandas, datetime, math

if __name__ == "__main__":
    fileloc = None
    try:
        fileloc = input("File Location: ")
        print()
    except:
        print("Invalid File. Exiting Importer.")
        exit()

    recipes = pandas.read_csv(fileloc, header=0,dtype=str)

    for recipe in recipes.itertuples(index=False,name=None):
        ratings = []
        for rating in recipe[2:]:
            try:
                num = float(rating)
                if not math.isnan(num):
                    ratings.append(num)
            except:
                continue
        name = recipe[0]
        if len(ratings) == 0:
            ratings.append(5.0)
            name = name + "(unrated)"

        save_recipe(name, recipe[1], datetime.date.today().isoformat(), ratings)
        print(f"Imported {name}")

