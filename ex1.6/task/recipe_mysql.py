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
def search_recipe(conn, cursor)



# Updating an existing recipe:
def update_recipe(conn, cursor)


# Deleting a recipe:
def delete_recipe(conn, cursor)
  

# view all recipes
def view_all_recipes(conn, cursor)