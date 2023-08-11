import mysql.connector

# DB creation
conn = mysql.connector.connect(
    host='localhost', 
    user='cf-python', 
    passwd='password')

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")

cursor.execute("USE task_database")

cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes(
id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(50),
ingredients VARCHAR(255),
cooking_time INT,
difficulty VARCHAR(20)
)''')

# Main Menu 

def main_menu(conn, cursor):
  choice = ""
  while(choice != "quit"):
    print("\n======================================================")
    print("\nMain Menu:")
    print("-------------")
    print("Pick a choice:")
    print("   1. Create a new recipe")
    print("   2. Search for a recipe by ingredient")
    print("   3. Update an existing recipe")
    print("   4. Delete a recipe")
    print("   5. View all recipes")
    print("\n   Type 'quit' to exit the program.")
    choice = input("\nYour choice: ")
    print("\n======================================================\n")

    if choice == "1":
      create_recipe(conn, cursor)
    elif choice == "2":
      search_recipe(conn, cursor)
    elif choice == "3":
      update_recipe(conn, cursor)
    elif choice == "4":
      delete_recipe(conn, cursor)
    elif choice == "5":
      view_all_recipes(conn, cursor)

# Creating a new recipe:
def create_recipe(conn, cursor):
    #recipe_ingredients = []

    # Asks the user to input recipe name
    name = str(input("Enter the name of the recipe: "))

    # Asks the user to input cooking time
    try:
        cooking_time = int(input("Cooking time in minutes: "))
    except ValueError:
        print('Please enter a valid number for cooking time')
        return None

    # Asks the user in input ingredients
    ingredients = (input("Enter the ingredients for your recipe, separated by a comma: ").split(", "))
    if not ingredients:
        print("Please provide at least one ingredient")
        return None
    lowercase_ingredients = [ingredient.lower() for ingredient in ingredients]
    difficulty = calculate_difficulty(cooking_time, lowercase_ingredients)
    recipe_ingredients_str = ", ".join(lowercase_ingredients)

    # SQL and database insertion
    sql = 'INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)'
    val = (name, recipe_ingredients_str, cooking_time, difficulty)
    cursor.execute(sql, val)
    conn.commit()
    print("Recipe saved into the database.")

def calculate_difficulty(cooking_time, ingredients):
        num_ingredients = len(ingredients)
        if cooking_time < 10:
            if num_ingredients < 4:
                difficulty = "Easy"
            else:
                difficulty = "Medium"
        else:
            if num_ingredients < 4:
                difficulty = "Intermediate"
            else:
                difficulty = "Hard"

        print("Difficulty level: ", difficulty)
        return difficulty


# Searching for a recipe by ingredient
def search_recipe(conn, cursor):
    all_ingredients = []

    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()

    # loops through the results list and for each recipe ingredients tuple
    for recipe_ingredients_list in results:
        for recipe_ingredients in recipe_ingredients_list:
            recipe_ingredient_split = recipe_ingredients.split(", ")
            all_ingredients.extend(recipe_ingredient_split)


    # Remove all duplicates from the list
    all_ingredients = set(all_ingredients)

     # Convert the set back to a list and sort it
    all_ingredients_list = sorted(list(all_ingredients))


    print("\nAll ingredients list:")
    print("------------------------")

    for index, ingredient in enumerate(all_ingredients_list):
        print(str(index+1) + ". " + ingredient)

    try:
        ingredient_number = int(input("\nEnter the number corresponding to the ingredient you want: "))

        if 1 <= ingredient_number <= len(all_ingredients_list):
            selected_ingredient = all_ingredients_list[ingredient_number - 1]
            print(f"\nYou selected the ingredient: {selected_ingredient}")

    except IndexError:
        print('The number you entered is not on the list.')
    except ValueError:
        print('Invalid input. Please enter a valid number.')
    except:
        print('An error occurred while finding your ingredient.')

    else:
        print("\nThe recipe(s) below include(s) the selected ingredient: ")
        print("-------------------------------------------------------")

    cursor.execute("SELECT * FROM Recipes WHERE ingredients LIKE %s", ('%' + selected_ingredient + '%', ))

    results_recipes_with_ingredient = cursor.fetchall()

    # Displays the data from each recipe found
    for row in results_recipes_with_ingredient:
      print("\nID: ", row[0])
      print("name: ", row[1])
      print("ingredients: ", row[2])
      print("cooking_time: ", row[3])
      print("difficulty: ", row[4])   
    

# Updating an existing recipe:
def update_recipe(conn, cursor):
    view_all_recipes(conn, cursor)

 # Asks the user to input the ID of the recipe he wants to update
    recipe_id_for_update = int((input("\nEnter the ID of the recipe you want to update: ")))

# Asks the user to input which column he wants to update among name, cooking_time and ingredients
    column_for_update = """str(input("\nChoose and enter which you would like to update among name, 
                            cooking time and ingredients: "))"""
    
     # Asks the user to input the new value
    updated_value = (input("\nEnter the new value for the recipe: "))

    # Update the chosen field in the database
    if column_for_update == "name":
        cursor.execute("UPDATE Recipes SET name = %s WHERE id = %s", (updated_value, recipe_id_for_update))
    elif column_for_update == "cooking_time":
        cursor.execute("UPDATE Recipes SET cooking_time = %s WHERE id = %s", (updated_value, recipe_id_for_update))
    elif column_for_update == "ingredients":
        cursor.execute("UPDATE Recipes SET ingredients = %s WHERE id = %s", (updated_value, recipe_id_for_update))


    # Recalculate difficulty and update the difficulty field
    cursor.execute("SELECT cooking_time, ingredients FROM Recipes WHERE id = %s", (recipe_id_for_update,))
    result = cursor.fetchone()
    if result:
        cooking_time, ingredients = result
        lowercase_ingredients = [ingredient.lower() for ingredient in ingredients.split(", ")]
        difficulty = calculate_difficulty(cooking_time, lowercase_ingredients)
        cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s", (difficulty, recipe_id_for_update))
        conn.commit()
        print(f"The recipe {column_for_update} has been updated!")

    else:
        print("Recipe not found.")




# Deleting a recipe:
def delete_recipe(conn, cursor):
    view_all_recipes(conn, cursor)
    recipe_id_for_deletion = (
        input("\nEnter the ID of the recipe you want to delete: "))
    cursor.execute("DELETE FROM Recipes WHERE id = (%s)",
                   (recipe_id_for_deletion, ))

    conn.commit()
    print("\nRecipe successfully deleted from the database.")
  

# Main Code here

main_menu(conn, cursor)
print("See ya soon\n")