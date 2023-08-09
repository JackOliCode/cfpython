class Recipe:
    all_ingredients = set()
    
    def __init__(self, name):
        self._name = name
        self._ingredients = []
        self._cooking_time = 0
        self._difficulty = None

    def calculate_difficulty(self):
        num_ingredients = len(self._ingredients)
        if self._cooking_time < 10:
            if num_ingredients < 4:
                self._difficulty = "Easy"
            else:
                self._difficulty = "Medium"
        else:
            if num_ingredients < 4:
                self._difficulty = "Intermediate"
            else:
                self._difficulty = "Hard"
    
    def add_ingredients(self, *ingredients):
        self._ingredients.extend(ingredients)
        self.update_all_ingredients()
        self.calculate_difficulty()

    def get_ingredients(self):
        return self._ingredients
    
    def search_ingredient(self, ingredient):
        return ingredient in self._ingredients
    
    def update_all_ingredients(self):
        for ingredient in self._ingredients:
            Recipe.all_ingredients.add(ingredient)
    
    def get_difficulty(self):
        if not self._difficulty:
            self.calculate_difficulty()
        return self._difficulty
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name
    
    def get_cooking_time(self):
        return self._cooking_time
    
    def set_cooking_time(self, cooking_time):
        self._cooking_time = cooking_time
        self.calculate_difficulty()
    
    def __str__(self):
        return f"""Recipe Name: {self._name}
Ingredients: {', '.join(self._ingredients)}
Cooking Time: {self._cooking_time} minutes
Difficulty: {self.get_difficulty()}
"""
    

def recipe_search(data, search_term):
    print(f"Recipes that contain '{search_term}':\n")
    for recipe in data:
        if recipe.search_ingredient(search_term):
            print(recipe)

# Main code

# list of recipes
tea = Recipe("Tea")
coffee = Recipe("Coffee")
cake = Recipe("Cake")
smoothie = Recipe("Banana Smoothie")

# Set ingredients and cooking time using setters
tea.add_ingredients("Tea Leaves", "Sugar", "Water")
tea.set_cooking_time(5)

coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
coffee.set_cooking_time(5)

cake.add_ingredients("Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk")
cake.set_cooking_time(50)

smoothie.add_ingredients("Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes")
smoothie.set_cooking_time(5)

# Add recipes to list
recipes_list = [tea, coffee, cake, smoothie]

# Display string representation of each recipe
for recipe in recipes_list:
    print(recipe)

# Search for recipes that contain certain ingredients
for ingredient in ["Water", "Sugar", "Bananas"]:
    recipe_search(recipes_list, ingredient)