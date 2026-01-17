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


class Point:
    def __init__(self, x: int, y: int, z: int = 0):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, value: Point):
        return self.x == value.x and self.y == value.y and self.z == value.z
    
    def __ne__(self, value: Point):
        return self.x != value.x or self.y != value.y or self.z != value.z
    
    def __hash__(self):
        return hash((self.x, self.y, self.y))