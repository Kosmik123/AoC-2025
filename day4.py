from helpers import load_input


class Room:
    def __init__(self, input: str):
        lines = input.split('\n')
        self.width = len(lines[0])
        self.height = len(lines)
        self.data = []
        for line in lines:
            for ch in line:
                self.data.append(ch)

    def is_inside(self, x: int, y: int) -> bool:
        return x >= 0 and y >= 0 and x < self.width and y < self.height

    def get_character(self, x: int, y: int) -> str:
        assert self.is_inside(x, y)

        return self.data[y * self.width + x]

    def is_occupied(self, x: int, y: int) -> bool:
        character = self.get_character(x, y)
        return character == '@'

    def set_occupied(self, x: int, y: int, occupy: bool = True):
        assert self.is_inside(x, y)
        self.data[y * self.width + x] = '@' if occupy else '.'



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

total_accessible_rolls_count = 0
room = Room(input)
while True:
    accessible_positions = []
    detected_rolls_count = 0
    for y in range(room.width):
        for x in range(room.height):
            if room.is_occupied(x, y):
                neighbours_count = count_neighbours(room, x, y)
                if neighbours_count < 4:
                    detected_rolls_count += 1
                    accessible_positions.append((x, y))

    for x, y in accessible_positions:
        room.set_occupied(x, y, False)

    print(detected_rolls_count)
    total_accessible_rolls_count += detected_rolls_count
    if detected_rolls_count == 0:
        break

print(total_accessible_rolls_count)
