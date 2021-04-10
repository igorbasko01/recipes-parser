from recipes_parser.model.ingredient import Ingredient
from recipes_parser.repository.neo4j_repo import Neo4jRepository


class TestNeo4jRepo:
    def test_ingredients_merge_stmt_creation(self):
        ingredients = [
            Ingredient("Potato"),
            Ingredient("Tomato"),
            Ingredient("Onion")
        ]

        merges = Neo4jRepository._create_ingredients_merge_statements(ingredients)
        assert merges == [
            "MERGE (i0:Ingredient {'name': 'Potato'})",
            "MERGE (i1:Ingredient {'name': 'Tomato'})",
            "MERGE (i2:Ingredient {'name': 'Onion'})",
        ]

    def test_relationship_statement_creation(self):
        result = Neo4jRepository._create_recipe_to_ingredient_relationship_statements(3)
        assert result == "CREATE (r0)-[:USES]->(i0),(r0)-[:USES]->(i1),(r0)-[:USES]->(i2)"
