from typing import List
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supply_set = set(supplies)
        result = []
        recipe_ingredients = {recipes[i]: ingredients[i] for i in range(len(recipes))}
        while True:
            new_recipes = []
            for recipe, required_ingredients in recipe_ingredients.items():
                if all(ingredient in supply_set for ingredient in required_ingredients):
                    if recipe not in supply_set:
                        supply_set.add(recipe)
                        new_recipes.append(recipe)
            if not new_recipes: break
            result.extend(new_recipes)
        return result