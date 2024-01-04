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
 


def remove_item(fridge_items, item_name, item_quantity):    #Aivaras
    if item_name in fridge_items and fridge_items[item_name] >= item_quantity:
        fridge_items[item_name] -= item_quantity
        if fridge_items[item_name] == 0:
            del fridge_items[item_name] 
        print(f"{item_name} was removed from the fridge.")
    else:
        print(f"{item_name} does not exist or not enough quantity left.")
        return fridge_items
  
def search_item(fridge_items, item_name: str):    #Maksim
    if item_name in fridge_items:
        print(f"{item_name} is in the fridge")
    else:
        print(f"No {item_name} was found in the fridge")


def print_items(fridge_items): #Petras
    print('Contents of the fridge:')
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
