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

beams = [start_col]
split_count = 0
for row in range(len(lines)):
    new_beams: list[int] = []
    line = lines[row]
    for beam_col in beams:
        if line[beam_col] == '^':
            split_count += 1
            print("split at:", row, beam_col)
            if beam_col >= 0:
                add_distinct(new_beams, beam_col - 1) 
            if beam_col < len(line) - 1:
                add_distinct(new_beams, beam_col + 1)
        else: 
            add_distinct(new_beams, beam_col)

    beams = new_beams

print(split_count)