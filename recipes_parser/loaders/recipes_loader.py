import logging
import recipes_parser.utils.file_ops as fops

from typing import List
from recipes_parser.model.recipe import Recipe
from recipes_parser.model.ingredient import Ingredient


class RecipesLoader:
    def __init__(self, recipes_path, repository):
        self.recipes_path = recipes_path
        self.repository = repository

    def run(self):
        recipes = self._prepare_recipes()
        self._store_recipes(recipes)

    def _prepare_recipes(self) -> List[Recipe]:
        dict_recipes = fops.read_json_file(self.recipes_path)
        recipes = [
            Recipe(
                recipe['title'].replace("'", ""),
                f"https://www.youtube.com/watch?v={recipe['id']}",
                self._prepare_ingredients(recipe['predicted_ingredients']))
            for recipe in dict_recipes
        ]

        ingredients_amount = sum([len(recipe.ingredients) for recipe in recipes])
        logging.info(f"Found {len(recipes)} recipes with {ingredients_amount} named ingredients total.")

        return recipes

    def _store_recipes(self, recipes: List[Recipe]):
        for recipe in recipes:
            logging.info(f"Storing the following recipe: {recipe}")
            self.repository.add_recipe_with_ingredients(recipe)

    @staticmethod
    def _prepare_ingredients(predicted_ingredients):
        parsed_ingredients = [Ingredient(ingredient['name'].replace("'", ""))
                              for ingredients in predicted_ingredients
                              for ingredient in ingredients if 'name' in ingredient]
        return parsed_ingredients

