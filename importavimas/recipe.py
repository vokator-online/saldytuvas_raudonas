from product import Product
from fridge import Fridge

class Recipe:
    ingredients = []
    instructions = []

    def add_ingredient(self, product:Product):
        self.ingredients.append(product)

    def change_ingredient_quantity(self, ingredient_id:int, new_quantity:float):
        self.ingredients[ingredient_id].quantity = new_quantity

#Balys new function update
    def check_ingredient(self, ingredient_name:str) -> (int, Product):
        for ingredient_id, ingredient in enumerate(self.ingredients):
            if ingredient_name == ingredient.name:
                return ingredient_id, ingredient
        return None, None

#Balys/Petras quantity/print update
    def remove_ingredient(self, name:str, quantity:float):
        self.print_recipe()
        ingredient_id, ingredient = self.check_ingredient(name)
        if ingredient is not None:
            if ingredient.quantity >= quantity:
                ingredient.quantity -= quantity
                print(f"{quantity}x{ingredient} was removed from recipe")
                if ingredient.quantity == 0:
                    self.ingredients.remove(ingredient)
                    print(f"All the {ingredient} was removed")
            else:
                print(f"Not enough {name} in the recipe.")
        else:
            print(f"Ingredient {name} does not exist in the recipe.")

    def print_recipe(self):
        for index, ingredient in enumerate(self.ingredients, start=1):
            print(f"{index}, {ingredient}")
