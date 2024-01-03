def search_item(string_entered: str, fridge_content={'None':0.00} ):
    for key in fridge_content:
        if str(key).startswith(string_entered):
            print(f"Item found {key} with quantity {fridge_content[key]}!")
        else:
            print("No items found!")