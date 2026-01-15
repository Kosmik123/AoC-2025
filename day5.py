from helpers import load_input


class SingleRange:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def can_join(self, other: SingleRange) -> bool:
        return self.start <= other.start <= self.end + 1 or other.start <= self.start <= other.end + 1 

    def join(self, other: SingleRange) -> None:
        self.start = min(self.start, other.start)
        self.end = max(self.end, other.end)

    def __str__(self):
        return f"({self.start}, {self.end})"


class IdRanges:
    def __init__(self):
        self.ranges: list[SingleRange] = []
        self.max_id = -1
        self.min_id = None

    def add_range(self, start: int, end: int):
        new_range = SingleRange(start, end)
        for i in range(len(self.ranges) - 1, -1, -1):
            other = self.ranges[i]
            if new_range.can_join(other):
                self.ranges.pop(i)
                new_range.join(other)

        self.ranges.append(new_range)
        
        if end > self.max_id:
            self.max_id = end
        if self.min_id == None or start < self.min_id:
            self.min_id = start

    def add_range_str(self, id_range: str):
        start, end = id_range.split('-')
        self.add_range(int(start), int(end))

    def __contains__(self, key: int) -> bool:
        for r in self.ranges:
            if r.start <= key <= r.end:
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


all_fresh_count = 0
for single_range in fresh.ranges:
    count = single_range.end - single_range.start + 1 
    print(count)
    all_fresh_count += count

print(all_fresh_count)