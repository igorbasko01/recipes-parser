from neo4j import GraphDatabase
from typing import List, Dict
from dataclasses import asdict
from recipes_parser.model.recipe import Recipe
from recipes_parser.model.ingredient import Ingredient


class Neo4jRepository:

    INGREDIENT = "Ingredient"
    RECIPE = "Recipe"

    def __init__(self, connection_config):
        con = connection_config
        self.driver = GraphDatabase.driver(con['url'], auth=(con['user'], con['password']))

    def close(self):
        self.driver.close()

    @staticmethod
    def _get_all_ingredients(tx):
        key_name = 'ingredient'
        return [record.data()[key_name]
                for record in tx.run(f"MATCH ({key_name}:{Neo4jRepository.INGREDIENT}) return {key_name}")]

    @staticmethod
    def _get_all_recipes(tx):
        key_name = 'recipe'
        return [record.data()[key_name]
                for record in tx.run(f"MATCH ({key_name}:{Neo4jRepository.RECIPE}) return {key_name}")]

    @staticmethod
    def _add_ingredient(tx, ingredient: Ingredient):
        pass

    def add_recipe_with_ingredients(self, recipe: Recipe, ingredients: List[Ingredient]):
        with self.driver.session() as session:
            result = session.write_transaction(self._add_recipe_with_ingredients, recipe, ingredients)
        print(result)

    @staticmethod
    def _add_recipe_with_ingredients(tx, recipe: Recipe, ingredients: List[Ingredient]):
        ingredients_merges = Neo4jRepository._create_ingredients_merge_statements(ingredients)
        recipe_merge = Neo4jRepository._create_recipe_merge_statement(recipe)
        relationships = Neo4jRepository._create_recipe_to_ingredient_relationship_statements(len(ingredients))
        return tx.run(f"{' '.join(ingredients_merges)} {recipe_merge} {relationships}")

    @staticmethod
    def _create_ingredients_merge_statements(ingredients: List[Ingredient]) -> List[str]:
        return [Neo4jRepository._create_merge_statement(f"i{i}", "Ingredient", asdict(ingredient))
                for i, ingredient in enumerate(ingredients)]

    @staticmethod
    def _create_recipe_merge_statement(recipe: Recipe) -> str:
        return Neo4jRepository._create_merge_statement("r0", Neo4jRepository.RECIPE, asdict(recipe))

    @staticmethod
    def _create_recipe_to_ingredient_relationship_statements(ingredients_amount: int) -> str:
        relationships = [f"(r0)-[:USES]->(i{i})" for i in range(ingredients_amount)]
        return f"CREATE {','.join(relationships)}"

    @staticmethod
    def _create_merge_statement(var_name: str, node_type: str, properties: Dict) -> str:
        return f"MERGE ({var_name}:{node_type} {properties})"

