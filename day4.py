from helpers import load_input


class Room:
    def __init__(self, input: str):
        lines = input.split('\n')
        self.width = len(lines[0])
        self.height = len(lines)
        self.data = ''.join(lines)

    def is_inside(self, x: int, y: int) -> bool:
        return x >= 0 and y >= 0 and x < self.width and y < self.height

    def get_character(self, x: int, y: int) -> str:
        assert self.is_inside(x, y)

        return self.data[y * self.width + x]

    def is_occupied(self, x: int, y: int) -> bool:
        character = self.get_character(x, y)
        return character == '@'
    

def count_neighbours(room: Room, x: int, y: int) -> int:
    count = 0
    for j in range(-1, 2):
        for i in range(-1, 2):
            if j == 0 and i == 0:
                continue
            nx = x + i
            ny = y + j
            if not room.is_inside(nx, ny):
                continue
            if room.is_occupied(nx, ny):
                count += 1 
    
    return count



input = '''..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.'''

input = load_input()

accessible_rolls_count = 0
room = Room(input)
for y in range(room.width):
    for x in range(room.height):
        if room.is_occupied(x, y):
            neighbours_count = count_neighbours(room, x, y)
            if neighbours_count < 4:
                accessible_rolls_count += 1

print(accessible_rolls_count)