def add_item(inventory, item_name, item_quantity):
    if item_name in inventory:
        inventory[item_name] += item_quantity
    else:
        inventory[item_name] = item_quantity

def remove_item(inventory, item_name, item_quantity):
    if item_name in inventory and inventory[item_name] >= item_quantity:
        inventory[item_name] -= item_quantity
        print(f"Removed {item_quantity} {item_name}(s) from the inventory.")
    else:
        print(f"Not enough {item_name} in the inventory or it does not exist.")

def check_quantity(inventory, item_name, required_quantity):
    if item_name in inventory:
        if inventory[item_name] >= required_quantity:
            print(f"There is enough {item_name} in the inventory.")
        else:
            print(f"Not enough {item_name} in the inventory.")
    else:
        print(f"{item_name} not found in the inventory.")

def print_inventory(inventory):
    if not inventory:
        print("The inventory is empty.")
    else:
        print("Inventory:")
        for item_name, item_quantity in inventory.items():
            print(f"{item_name}: {item_quantity}")

inventory = {}

while True:
    print('=== Inventory Management ===')
    print('0: Exit')
    print('1: Add Item')
    print('2: Remove Item')
    print('3: Check Quantity')
    print('4: Print Inventory')
    choice = input('Enter your choice: ')
    
    if choice == '0':
        break
    elif choice == '1':
        item_name = input('Enter item name: ')
        item_quantity = int(input('Enter item quantity: '))
        add_item(inventory, item_name, item_quantity)
    elif choice == '2':
        item_name = input('Enter item name: ')
        item_quantity = int(input('Enter item quantity: '))
        remove_item(inventory, item_name, item_quantity)
    elif choice == '3':
        item_name = input('Enter item name: ')
        required_quantity = int(input('Enter required quantity: '))
        check_quantity(inventory, item_name, required_quantity)
    elif choice == '4':
        print_inventory(inventory)
    else:
        print("Invalid choice. Please try again.")
