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

    def remove_ingredient(self, ingredient_id:int):
        self.ingredients.pop(ingredient_id)


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

    def remove_product(self, name:str, quantity:float):
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

    while True:
        print('''
              =+=+=Choose what you want to do=+=+=
              0 = Exit.
              1 = Add a product.
              2 = Remove a product.
              3 = Check recipe is crafttable.
              4 = Print content of the fridge.
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
            recipe = Recipe()
            recipe.add_ingredient(Product("Ingredient "))
            fridge.check_recipe(recipe)
        elif choice == '4':
            fridge.print_contents()
        else:
            print("Bad choice, try again")


main()
    