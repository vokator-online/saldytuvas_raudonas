def main():
    while True:
        print('''
              asd
              asd
              asd
              asd
              ''')
        choice = input("Choice: ")
        if choice.startswith("exit"):
            break
        elif choice.startswith("insert"):
            fridge_items = insert_item(input("Item name:"), input('Item quantity:'))
        elif choice.startswith("remove"):
            remove_item()
        elif choice.startswith("search"):
            search_item()
        elif choice.startswith("print"):
            print_items()
        else:
            print("Bad choice, try again")