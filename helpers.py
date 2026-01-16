import inspect
from pathlib import Path

def load_input() -> str:
    path = inspect.stack()[1].filename 
    filename = Path(path).stem + " input.txt"
    with open(filename, 'r') as file:
        data = file.read()
    return data         


def add_distinct(list: list, item):
    if item not in list:
        list.append(item)
