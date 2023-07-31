import pickle

#Define a function called take_recipe, which takes input from the user
def take_recipe():
    name = input("Recipe name: ")
    try:
        cooking_time = int(input("Cooking time in minutes: "))
    except ValueError:
        print('Please enter a valid number for cooking time')
        return None
    ingredients = input("Ingredients (separated by a comma): ").split(", ")
    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients
    }
    recipe['Difficulty'] = calc_difficulty(recipe)
    return recipe

#Define the function calc_diffficulty(), where the difficulty is returned as Easy, Medium, Intermediate or Hard
def calc_difficulty(recipe):
    if recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
      difficulty = 'Easy'
    elif recipe['cooking_time'] < 10 and len(recipe['ingredients']) >= 4:
      difficulty = 'Medium'
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
      difficulty = 'Intermediate'
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) >= 4:
      difficulty = 'Hard'
    return difficulty

recipes_list = []
all_ingredients = []

#try-except-else-finally below
filename = input('Please enter the name of the file containing your receipes: ')
try: 
    recipes_file = open(filename, 'rb')
    data = pickle.load(recipes_file)
except FileNotFoundError:
    print("File doesn't exist - creating a file for you.")
    data = {'recipes_list': [], 'all_ingredients': []}
except:
    print("An unexpected error occurred - creating a file for you.")
    data = {'recipes_list': [], 'all_ingredients': []}
else:
    recipes_file.close()
finally:  
    recipes_list = data['recipes_list']
    all_ingredients = data['all_ingredients']

#ask the user how many recipes they would like to enter
n = int(input("How many recipes would you like to enter?: "))

# loop that runs i times for user input & runs take_recipe func. 
# picks out any ingredients not in all_ingredients and adds them. 
# Adds recipe to recipes_list
for i in range(n):
    recipe = take_recipe()
    for ingredient in recipe['ingredients']:
        if not ingredient in all_ingredients:
            all_ingredients.append(ingredient)
    recipes_list.append(recipe)

# Gather the updated recipes_list and all_ingredients into the dictionary called data.
data = {'recipes_list': recipes_list, 'all_ingredients': all_ingredients}

new_file_name = input('Enter a name for your new recipe file.')
with open(new_file_name, 'wb') as f:
    pickle.dump(data, f)