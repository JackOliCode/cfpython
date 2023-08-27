from django.db import models

#model below
class Recipe (models.Model):
    name = models.CharField(max_length=120)
    cooking_time = models.FloatField(help_text='in minutes')
    ingredients = models.CharField(max_length=350)
   
    # calc difficulty function

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

            return difficulty

    def __str__(self):
        return str(self.name)
