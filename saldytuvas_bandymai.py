def remove_iems(produktai: list, task_index: int) -> list:
    removed_task = produktai.pop(task_index)
    print(f"Removed task: {removed_task['name']}")
    return produktai

def remove_item(item_name, item_quantity):    #Aivaras
    if item_name in fridge_items and fridge_items[item_name] >= item_quantity:
        fridge_items[item_name] -= item_quantity
        print(f"Removed {item_quantity}x {item_name} from the fridge.")
    else:
        print(f"Not enough {item_name} in the fridge or it does not exist.")
