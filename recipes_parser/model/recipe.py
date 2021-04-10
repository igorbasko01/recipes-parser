from typing import List
from dataclasses import dataclass
from recipes_parser.model.ingredient import Ingredient


@dataclass
class Recipe:
    name: str
    url: str
    ingredients: List[Ingredient]
