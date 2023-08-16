#==================== 
# Set Up Script, SQLAlchemy & Session Factory
#==================== 

from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import Integer, String
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine = create_engine("mysql://cf-python:password@localhost/my_database")
Base = declarative_base()
Session = sessionmaker(bind=engine)


#==================== 
# Define the Recipe class
#==================== 

class Recipe(Base):
  __tablename__ = "final_recipes"

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(50))
  ingredients = Column(String(255))
  cooking_time = Column(Integer)
  difficulty = Column(String(20))

  def __repr__(self):
    return "<Recipe ID: " + str(self.id) + "-" + self.name + ">"

  def __str__(self):
    output = "="*15 + \
        "\nName: " + str(self.name) + \
        "\nCooking time (minutes): " + str(self.cooking_time) + \
        "\nDifficulty: " + str(self.difficulty) + \
        "\nIngredients: " + str(self.ingredients)
    return output
  
  def calculate_difficulty(self):
        num_ingredients = len(self.ingredients.split(','))
        if self.cooking_time < 10:
            if num_ingredients < 4:
                difficulty = "Easy"
            else:
                difficulty = "Medium"
        else:
            if num_ingredients < 4:
                difficulty = "Intermediate"
            else:
                difficulty = "Hard"

        self.difficulty = difficulty
  

  def return_ingredients_as_list(self):
        if not self.ingredients:
            print("It looks like your ingredients list is empty.")
            return []        
        else:
            return self.ingredients.split(', ')

#===================
# Create tables of all models defined
#===================

Base.metadata.create_all(engine)

#===================
# Create a session
#===================

session = Session()

#===================
#Main Operations as Functions
#===================

#===================
# Create Recipe
#===================

def create_recipe():

    while True:
        name = input("Enter the recipe name (up to 50 characters): ")
        if len(name) <= 50:
            break
        else:
            print("Name exceeds the maximum length. Please enter a shorter name.")

    while True:
        cooking_time = input("Enter the cooking time (in minutes): ")
        if cooking_time.isnumeric():
            break
        else:
            print("Invalid cooking time. Please enter a valid number.")

    while True:
        num_ingredients = input("Enter the number of ingredients for this recipe: ")
        if num_ingredients.isnumeric():
            num_ingredients = int(num_ingredients)
            break
        else:
            print("Invalid number of ingredients. Please enter a valid number.")

    recipe_ingredients = []  # Temporary list to collect ingredients renamed to avoid confusion

    for n in range(num_ingredients):
        ingredient = input(f"Enter ingredient {n + 1}: ").lower()
        recipe_ingredients.append(ingredient)

    ingredients_string = ", ".join(recipe_ingredients)

    recipe_entry = Recipe(
        name = name,
        ingredients = ingredients_string,
        cooking_time = int(cooking_time)
    )

    recipe_entry.calculate_difficulty()

    session.add(recipe_entry)
    session.commit()
    
    print(f'{name} added to Recipes!')

#===================
# View Recipes
#===================
def view_all_recipes():
    all_recipes = session.query(Recipe).all()
    
    if not all_recipes:
        print("There aren't any entries in the database.")
        return None
    
    for recipe in all_recipes:
        print(recipe)

#===================
# Search by Ingredient
#===================
def search_by_ingredients():

    if session.query(Recipe).count() == 0:
        print("There is no recipe in the database")
        return None
    
    else:
        results = session.query(Recipe.ingredients).all()

        all_ingredients = []

        for recipe_ingredients_list in results:
            for recipe_ingredients in recipe_ingredients_list:
                recipe_ingredient_split = recipe_ingredients.split(", ")
                recipe_ingredient_set = set(recipe_ingredient_split)
                all_ingredients_list = sorted(list(recipe_ingredient_set))
                all_ingredients.extend(all_ingredients_list)

        print("\nBelow are all the ingredients stored. You can search for recipes by ingredient number.")
        print("="*15)

        for index, ingredient in enumerate(all_ingredients):
            print(str(index+1) + ". " + ingredient)

        try:
            ingredient_numbers_input = (input("\nEnter the numbers corresponding to the ingredients you'd like to search, seperated by a space: "))
            ingredient_numbers_split = ingredient_numbers_input.split(" ")

            selected_numbers = list(map(int, ingredient_numbers_split))

            search_ingredients = []

            for number in selected_numbers:
                if 1 <= number <= len(all_ingredients):
                    selected_ingredient = all_ingredients[number - 1]
                    search_ingredients.append(selected_ingredient)
                else:
                    print(f"Ingredient with number {number} is not on the list.")
            
            print(f"\nYou selected the ingredient(s): {search_ingredients}")

            # Create a list of like conditions to search for each ingredient

            conditions = []
            
            for ingredient in search_ingredients:
                like_term = f"%{ingredient}"
                conditions.append(Recipe.ingredients.like(like_term))
            
            # Retrieve recipes based on the conditions
            searched_recipes = session.query(Recipe).filter(*conditions).all()
            
            if not searched_recipes:
                print("No recipes found with the selected ingredients.")
            else:
                print("\nSearched Recipes: ")
                for recipe in searched_recipes:
                    print(recipe)

        except ValueError:
            print("Invalid input. Please enter valid numbers.")

#===================
# Edit recipes
#===================


#===================
# Delete recipe
#===================
