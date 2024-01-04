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
            insert_item(fridge_items, item_name, float(item_quantity)) 
        elif choice.startswith("remove"):
            item_name = input("Item name:")
            item_quantity = input('Item quantity:')
            remove_item(fridge_items, item_name, float(item_quantity)) 
        elif choice.startswith("search"):
            item_name = input("Item name:")
            search_item(fridge_items, item_name)
        elif choice.startswith("print"):
            print_items(fridge_items)
        else:
            print("Bad choice, try again")

            
def insert_item(fridge_items, item_name: str, item_quantity: float): #Balys
    if item_name in fridge_items:
        fridge_items[item_name] += item_quantity
        print(f"{item_name} was already in the fridge and we added {item_quantity} more")
    else:
        fridge_items[item_name] = item_quantity
        print(f"{item_quantity}x {item_name} was added to the fridge")
 


def remove_item(item_name, item_quantity):    #Aivaras
    if item_name in fridge_items[item_name] >= item_quantity:
        fridge_items[item_name] -= item_quantity
        print(f"Removed {item_quantity}x {item_name} from the fridge.")
    else:
        print(f"Not enough {item_name} in the fridge or it does not exist.")
        return fridge_items
  
def search_item(fridge_items, item_name: str):    #Maksim
    if item_name in fridge_items:
        print("Dog is in the house")
    else:
        print(f"No {item_name} was found")


def print_items(fridge_items): #Petras
    print('Šaldytuve esantys produktai:')
    for index, (item_name, item_quantity) in enumerate(fridge_items.items(), start=1):
        print(f'{index}. {item_name} : {item_quantity}')


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
