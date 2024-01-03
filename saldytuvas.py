fridge_items = {}

def main():  # Valdemaras
    while True:
        print('''
              ----Choose what you want to do with the fridge----
              exit = Exit.
              insert = Insert a new product into the fridge.
              remove = Remove item from the fridge.
              search = Search fridge for a product and quantity.
              print = Print all the contents of the fridge.
              ''')
        choice = input("Your choice: ")
        if choice.startswith("exit"):
            break
        elif choice.startswith("insert"):
            item_name = input("Item name:")
            item_quantity = input('Item quantity:')
            insert_item(item_name, float(item_quantity)) 
        elif choice.startswith("remove"):
            remove_item(input("Item name:"), float(input('Item quantity:')))
        elif choice.startswith("search"):
            search_item()
        elif choice.startswith("print"):
            print_items()
        else:
            print("Bad choice, try again")

            
def insert_item(item_name: str, item_quantity: float): #Balys
    fridge_items[item_name] = item_quantity
    print(f"{item_quantity}x{item_name} was added to the fridge")
    return fridge_items


def remove_item(item_name, item_quantity):    #Aivaras
    item_remove = {"Item name:": item_name, "Item quantity": item_quantity}
    if item_name in fridge_items and fridge_items[item_name] >= item_quantity:
        fridge_items[item_name] -= item_quantity
        print(f"{item_name} išimtas iš šaldytuvo.")
    else:
        print(f"{item_name} kiekio šaldytuve nepakanka arba jis neegzistuoja.")
        return fridge_items
  
def search_item(fridge_items, item_name: str, item_quantity: float):    #Maksim
    if item_name in fridge_items:
        return fridge_items[item_name] >= item_quantity
    else:
        return False


def print_items(fridge_items): #Petras
    if  fridge_items == {}:

        print('Šaldytuvas yra tuščias. Badauk arba įdėk ką nors')
    else:
        print('Šaldytuve esantys produktai:')
        for index, (item_name, item_quantity) in enumerate(fridge_items.items(), start=1):
            print(f'{index}. {item_name} : {item_quantity}')
            return

if __name__ == "__main__":
    main()

""" Komandinio darbo užduotis
===[ Šaldytuvas ]===

Reikalavimai:

* Šaldytuvo turinys - žodynas, kurio raktas yra produkto pavadinimas, reikšmė - kiekis (float).
* Pridėti produktą į šaldytuvą. Pridedant egzistuojantį produktą, kiekiai sudedami su esančiais.
* Išimti produktą iš šaldytuvo. Išimant egzistuojantį produktą, kiekis atitinkamai sumažinamas.
* Patikrinti, ar reikiamas produkto kiekis yra šaldytuve.
* Išspausdinti visą šaldytuvo turinį su kiekiais.

BONUS:

* Patikrinti, ar receptas išeina. 
** Recepto įvedimas vyksta viena eilute, kuri po to išdalinama. Pva.: Sūris: 0.5, Pomidoras: 2, Duona: 0.4
** Jeigu receptas neišeina, išvardinti kiek ir kokių produktų trūksta.

"""
