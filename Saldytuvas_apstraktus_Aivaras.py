class Product:
    def __init__(self, name:str, quantity:float, **kwargs) -> None:
        self.name = name
        self.quantity = quantity
        self.unit_of_measurement = 'unit' # options: kg, g, L, ml
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        return f"{self.name}: {self.quantity}"
    
    def __repr__(self) -> str:
        return f"({self.name}, {self.quantity})"


class Recipe:
    ingredients = []
    instructions = []

    def add_ingredient(self, product:Product):
        self.ingredients.append(product)

    def change_ingredient_quantity(self, ingredient_id:int, new_quantity:float):
        self.ingredients[ingredient_id].quantity = new_quantity

    def check_ingredient(self, ingredient_name: str) -> (int, Product):
        for ingredient_id, ingredient in enumerate(self.ingredients):
            if ingredient_name == ingredient.name:
                return ingredient_id, ingredient
        return None, None

    def remove_ingredient(self, name: str, quantity: float):
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
            print(f'{index}, {ingredient}')


class Fridge:
    contents = []

    def check_product(self, product_name:str) -> (int, Product):
        for product_id, product in enumerate(self.contents):
            if product.name == product_name:
                return product_id, product
        return None, None
    
    def check_product_quantity(self, product:Product, quantity:float):
        return product.quantity - quantity

    def add_product(self, name:str, quantity:float):
        product_id, product = self.check_product(name) # nenaudojamus kintamuosius galima vadinti tiesiog _
        if product is not None:
            product.quantity += quantity
        else:
            self.contents.append(Product(name, quantity))
            print(f"{name}x {quantity} was added to the fridge.")

    def print_contents(self):
        for index, line in enumerate(self.contents, start=1):
            print(f"{index} - {line}")

    def remove_product(self, name:str, quantity:float):
        self.print_contents()
        product_id, product = self.check_product(name)
        if product is not None:
            if product.quantity >= quantity:
                product.quantity -= quantity
                if product.quantity == 0:
                    self.contents.pop(product_id)
                print(f"Removed {quantity} {product.unit_of_measurement} of {name} form the fridge.")
            else:
                print(f"Not enough {name} quantity in the fridge.")
        else:
            print(f"{name} dos not exist in the fridge.")
    
    def print_contents(self):
        print('Fridge content: ')
        for index, product in enumerate(self.contents, start=1):
            print(f'{index}, {product}')

    def check_recipe(self, recipe:Recipe):
        for ingredient in recipe.ingredients:
            product_id, product = self.check_product(ingredient.name)
            if product is not None:
                if product.quantity >= ingredient.quantity:
                    print(f"{ingredient.name} is in fridge.")
                else:
                    print(f"Not enough {ingredient.name} quoantity.")
            else:
                print(f"{ingredient.name} is not in the fridge.")
            



def main():
    fridge = Fridge()
    recipe = Recipe()

    while True:
        print('''
              =+=+=Choose what you want to do=+=+=
              0 = Exit.
              1 = Add a product.
              2 = Remove a product.
              3 = Check recipe is crafttable.
              4 = Print content of the fridge.
              5 = Add products to recipe.
              6 = Remove products from recipe.
              7 = Change ingredient quantity of recipe.
              8 = Print current recipe.
              ''')
        choice = input("Your choice: ")

        if choice == '0':
            break
        elif choice == '1':
            name = input("Product name:")
            quantity = float(input('Product quantity:'))
            fridge.add_product(name, quantity)
        elif choice == '2':
            name = input("Product name: ")
            quantity = float(input('Product quantity:'))
            fridge.remove_product(name, quantity)
        elif choice == '3':
            fridge.check_recipe(recipe)
        elif choice == '4':
            fridge.print_contents()
        elif choice == '5':
            input_recipe_name = input("Product name: ")
            input_recipe_quantity = float(input("Product quantity: "))
            input_product = Product(input_recipe_name, input_recipe_quantity)
            recipe.add_ingredient(input_product)
        elif choice == '6':
            input_ingridient_id = int(input("Product ID: "))
            recipe.remove_ingredient(input_ingridient_id - 1)
        elif choice == '7':
            input_ingridient_id = int(input("Product ID: "))
            input_ingridient_quantity = float(input("Product quantity: "))
            recipe.change_ingredient_quantity(input_ingridient_id - 1, input_ingridient_quantity)
        elif choice == '8':
            recipe.print_recipe()
        else:
            print("Bad choice, try again")

        
Fridge().add_product("milk", 1)
Recipe().add_ingredient(Product("milk", 1))


main()

    