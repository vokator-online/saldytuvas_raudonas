class Product:
    def __init__(self, name:str, quantity:float, **kwargs) -> None:
        self.name = name
        self.quantity = quantity
        self.unit_of_measurement = 'vnt' # options: kg, g, L, ml
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        return f"{self.name}: {self.quantity} {self.unit_of_measurement}"
    
    def __repr__(self) -> str:
        return f"({self.name}, {self.quantity} {self.unit_of_measurement})"


class Recipe:
    def __init__(self):
        self.ingredients = []
        self.instructions = []

    def add_ingredient(self, product:Product):
        self.ingredients.append(product)

    def change_ingredient_quantity(self, ingredient_id:int, new_quantity:float):
        self.ingredients[ingredient_id].quantity = new_quantity

    def remove_ingredient(self, ingredient_id:int):
        self.ingredients.pop(ingredient_id)


class Fridge:
    contents = []

    def check_product(self, name:str) -> (int, Product):
        for product_id, product in enumerate(self.contents):
            if product.name == name:
                return product_id, name
        return None, None
    
    def check_product_quantity(self, product:Product, quantity:float):
        return product.quantity - quantity

    def add_product(self, name:str, quantity:float):
        _product_id, product = self.check_product(name) # nenaudojamus kintamuosius galima vadinti tiesiog _
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
                    self.contents.remove(product)
            else:
                print(f"Neužtenka produkto {name} šaldytuve.")
        else:
            print(f"Produkto{name} does not exist in the fridge.")

    def print_contents(self):
            print('Šaldytuve esantys produktai:')
            for index, product in enumerate(self.contents, start=1):
                print(f'{index}. {product}')

    def check_recipe(self, recipe: Recipe) -> bool:
        for ingredient in recipe.ingredients:
            fridge_product = self.check_product(ingredient.name)
            if fridge_product is None or fridge_product.quantity < ingredient.quantity:
                return False
        return True


def main():
    fridge = Fridge()

    while True:
        print('''
        ----Pasirinkite ką norite daryti šaldytuve----
        0 = Išeiti.
        1 = Įdėti produktą į šaldytuvą.
        2 = Išimti produktus iš šaldytuvo.
        3 = Peržiūrėti kas yra šaldytuve.
        4 = Patikrinti ar galima pagaminti pagal receptą.
        ''')
        choice = input("Your choice: ")

        if choice == "0":
            break
        elif choice == "1":
            name = input("Įveskite produktą: ")
            quantity = float(input("Įveskite produkto kiekį: "))
            fridge.add_product(name, quantity)
            print(f"Produkto {name} kiekis {quantity} buvo įdėtas į šaldytuvą.")
        elif choice == "2":
            name = input("Įveskite produkto pavadinimą, kurį norite išimti: ")
            quantity = float(input("Įveskite kiekį, kurį norite išimti: "))
            fridge.remove_product(iname)
        elif choice == "3":
            fridge.print_contents()
        elif choice == "4":
            recipe_name = input("Įveskite recepto pavadinimą: ")
            while True:
                ingredient_name = input("Įveskite produkto pavadinimą (jei baigėte, įveskite 'X'): ")
                if ingredient_name.lower() == 'X':
                    break
                ingredient_quantity = float(input(f"Įveskite kiekį ingridientui '{ingredient_name}': "))
                product = Product(ingredient_name, ingredient_quantity)
                recipe.add_ingredient(product)
            recipe = Recipe() 
            craftable = fridge.check_recipe(recipe)
            if craftable:
                print(f"{recipe_name} gali būti pagamintas iš šaldytuve esančių produktų")
            else:
                print(f"{recipe_name} negali būti pagamintas, nes trūksta produktų.")
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
   

