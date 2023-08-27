from django.test import TestCase
from .models import Recipe
from django.db import models

# Create your tests here.

class RecipeModelTest(TestCase):

    def setUpTestData():
        Recipe.objects.create(name='Smoothie', ingredients='Milk, Banana, Ice Cream', cooking_time='5', difficulty='Easy')

    def test_recipe_name(self):
        recipe_name = Recipe.objects.get(id=1)
        recipe_name_label = recipe_name._meta.get_field('name').verbose_name
        self.assertEqual(recipe_name_label, 'name')

    def test_recipe_ingredients(self):
        ingredients = Recipe.objects.get(id=1)
        recipe_ing_len = ingredients._meta.get_field('ingredients').max_length
        self.assertEqual(recipe_ing_len, 350)

    def test_recipe_cooking_time(self):
        cooking_time = Recipe.objects.get(id=1)
        recipe_cooking_time = cooking_time._meta.get_field('cooking_time')
        self.assertIsInstance(recipe_cooking_time, models.FloatField)


    def test_recipe_difficulty(self):
        difficulty = Recipe.objects.get(id=1)
        self.assertEqual(difficulty.calculate_difficulty(), 'Easy')
