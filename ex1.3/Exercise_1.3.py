#Initialize two empty lists
recipes_list = []
ingredients_list =[]

#Define a function called take_recipe, which takes input from the user
def take_recipe():
    name = input("Recipe name: ")
    cooking_time = int(input("Cooking time in minutes: "))
    ingredients = input("Ingredients (separated by a comma): ").split(", ")
    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients
    }
    return recipe

#ask the user how many recipes they would like to enter
n = int(input("How many recipes would you like to enter?: "))

# loop that runs i times for user input & runs take_recipe func. 
# picks out any ingredients not in ingredients_list and adds them. 
# Adds recipe to recipes_list
for i in range(n):
    recipe = take_recipe()
    for ingredient in recipe['ingredients']:
        if not ingredient in ingredients_list:
            ingredients_list.append(ingredient)
    recipes_list.append(recipe)


# loop that iterates through recipe_list and picks out recipes added in previous loop
# uses if-elif to determine difficulty
for recipe in recipes_list:
    if recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
      recipe['difficulty'] = 'Easy'
    elif recipe['cooking_time'] < 10 and len(recipe['ingredients']) >= 4:
      recipe['difficulty'] = 'Medium'
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
      recipe['difficulty'] = 'Intermediate'
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) >= 4:
      recipe['difficulty'] = 'Hard'    


# loop through recipes_list to pull out recipes. 
# print recipe data
for recipe in recipes_list:
   print('Recipe:', recipe['name'])
   print('Cooking time (min):', recipe['cooking_time'])
   print('Ingredients:')
   for ingredient in recipe['ingredients']:
      print(ingredient)
   print('Difficulty:', recipe['difficulty'])

def print_ingredients():
   ingredients_list.sort()
   print('Ingredients Available Across all Recipes:')
   print('------------------------------------------')
   for ingredient in ingredients_list:
      print(ingredient)

print_ingredients()
