from helpers import load_input

class IdRanges:
    def __init__(self):
        self.ranges = []

    def add_range(self, start: int, end: int):
        self.ranges.append((start,end))
    
    def add_range_str(self, id_range: str):
        start, end = id_range.split('-')
        self.add_range(int(start), int(end))

    def __contains__(self, key: int) -> bool:
        for start, end in self.ranges:
            if start <= key <= end:
                return True
        
        return False


def parse_input(input: str) -> tuple[IdRanges, list]:
    lines = input.split('\n')

    ranges = IdRanges()
    index = 0
    line = lines[0]
    while line != '' and index < len(lines):
        if '-' in line:
            ranges.add_range_str(line)
        index += 1
        line = lines[index]

    index += 1
    ids = []
    while index < len(lines):
        line = lines[index]        
        ids.append(int(line))
        index += 1

    return ranges, ids

input = '''3-5
10-14
16-20
12-18

1
5
8
11
17
32'''

input = load_input()


fresh, ingredients = parse_input(input)
fresh_count = 0
for ingredient in ingredients:
    if ingredient in fresh:
        print(ingredient, "is fresh")
        fresh_count += 1
    else:
        print(ingredient, "is spoiled")

print(fresh_count)