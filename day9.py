from helpers import load_input


def calculate_area(tile1: tuple[int, int], tile2: tuple[int, int]):
    width = abs(tile1[0] - tile2[0]) + 1
    length = abs(tile1[1] - tile2[1]) + 1
    return width * length

input = '''
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
'''[1:-1]

input = load_input()
lines = input.split('\n')

red_tiles_positions: list[(int, int)] = []

for line in lines:
    x, y = line.split(',')
    red_tiles_positions.append((int(x), int(y)))

highest_area = 0
for i in range(len(red_tiles_positions) - 1):
    tile1 = red_tiles_positions[i]
    for j in range(i + 1, len(red_tiles_positions)):
        tile2 = red_tiles_positions[j]         
        area = calculate_area(tile1, tile2)
        if area > highest_area:
            highest_area = area

print(highest_area)
