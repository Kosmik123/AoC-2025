from helpers import load_input

class Beam:
    def __init__(self, column: int, start_row: int, parent: Beam = None):
        self.column = column
        self.start_row = start_row
        self.parent = parent




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

# beams = [start_col]
# split_count = 0
# for row in range(len(lines)):
#     new_beams: list[int] = []
#     line = lines[row]
#     for beam_col in beams:
#         if line[beam_col] == '^':
#             split_count += 1
#             print("split at:", row, beam_col)
#             if beam_col >= 0:
#                 worlds_count += 1
#                 add_distinct(new_beams, beam_col - 1) 
#             if beam_col < len(line) - 1:
#                 worlds_count += 1
#                 add_distinct(new_beams, beam_col + 1)
#         else: 
#             add_distinct(new_beams, beam_col)

#     beams = new_beams

# print(split_count)
# print(worlds_count)

def simulate(beam: Beam) -> int:
    worlds_count = 0
    for row in range(beam.start_row, len(lines)):
        line = lines[row]
        ch = line[beam.column]
        if ch == '^':
            left = Beam(beam.column - 1, row)
            left.parent = beam
            right = Beam(beam.column + 1, row)
            right.parent = beam
            worlds_count += simulate(left)
            worlds_count += simulate(right)
            break
    else:
        worlds_count += 1
    
    return worlds_count


starting_beam = Beam(start_col, 0)
worlds_count = simulate(starting_beam)
print(worlds_count)