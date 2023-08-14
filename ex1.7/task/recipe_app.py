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
            return "It looks like your ingredients list is empty."
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