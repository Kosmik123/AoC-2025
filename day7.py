from helpers import load_input

def add_distinct(list: list, item):
    if item not in list:
        list.append(item)


input = '''
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............'''[1:]


input = load_input()

lines = input.split('\n')
start_col = lines[0].find('S')

worlds_per_splitter: dict[(int,int), int] = {}


def get_worlds_under_position(row: int, col: int):
    global lines
    global worlds_per_splitter
    for i in range(row + 1, len(lines)):
        if (i, col) in worlds_per_splitter:
            return worlds_per_splitter[(i, col)]
    
    return 1


def calculate_worlds_at_position(row: int, col: int):
    global lines
    global worlds_per_splitter
    line = lines[row]
    ch = line[col]   
    if ch != '^':
        return
    left_worlds = get_worlds_under_position(row, col - 1)
    right_worlds = get_worlds_under_position(row, col + 1)
    worlds_per_splitter[(row, col)] = left_worlds + right_worlds


def calculate_worlds_in_row(row: int):
    global lines
    for col in range(len(lines[row])):
        calculate_worlds_at_position(row, col)    


for row in range(len(lines) - 1, -1, -1):  
    calculate_worlds_in_row(row)

#print(worlds_per_splitter)

total_worlds = get_worlds_under_position(0, start_col)
print(total_worlds)