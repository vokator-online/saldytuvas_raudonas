def remove_iems(produktai: list, task_index: int) -> list:
    removed_task = produktai.pop(task_index)
    print(f"Removed task: {removed_task['name']}")
    return produktai