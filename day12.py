from helpers import load_input, compare_sets, Point


class PresentShapeVariant:
    def __init__(self, width: int, length: int, occupied: set[Point] = None):
        self.width = width
        self.length = length
        self.occupied = frozenset(occupied)

    def from_string(shape: str) -> PresentShapeVariant:
        lines = shape.split('\n')
        length = len(lines)
        width = 0
        occupied = set[Point]()
        for j in range(length):
            line = lines[j]
            line_width = len(line)
            if line_width > width:
                width = line_width
            for i in range(line_width):
                if line[i] == '#':
                    occupied.add(Point(i, j))
        shape_variant = PresentShapeVariant(width, length, occupied)
        return shape_variant
    
    def __str__(self):
        result_list = [['.' for _ in range(self.width)] for _ in range(self.length)] 
        for pos in self.occupied:
            result_list[pos.y][pos.x] = '#'
        s = '\n'.join(''.join(inner) for inner in result_list)
        return s

    def __eq__(self, value: PresentShapeVariant) -> bool:
        if self.length != value.length:
            return False
        if self.width != value.width:
            return False
        return self.occupied == value.occupied

    def __hash__(self):
        return hash(self.occupied)

    def flipped(self) -> PresentShapeVariant:
        occupied = set[Point]()
        for pos in self.occupied:
            occupied.add(Point(self.width-pos.x-1, pos.y))
        return PresentShapeVariant(self.width, self.length, occupied)

    def rotated_cw(self) -> PresentShapeVariant:
        occupied = set[Point]()
        for pos in self.occupied:
            occupied.add(Point(self.length-1-pos.y, pos.x))
        return PresentShapeVariant(self.length, self.width, occupied)



class PresentShape:
    def __init__(self, shape: str):
        self.variants = PresentShape.create_all_variants(PresentShapeVariant.from_string(shape))

    def create_all_variants(shape: PresentShapeVariant) -> set[PresentShapeVariant]:
        variants = set[PresentShapeVariant]()
        for variant in PresentShape.create_rotation_variants(shape):
            variants.add(variant)
        for variant in PresentShape.create_rotation_variants(shape.flipped()):
            variants.add(variant)
        return variants            

    def create_rotation_variants(shape: PresentShapeVariant) -> list[PresentShapeVariant]:
        variants = []
        variant = shape
        for _ in range(4):
            variants.append(variant)
            variant = variant.rotated_cw()
        return variants

input = '''
0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
'''[1:-1]



present_shapes = list[str]()

regions = list[tuple[int, int]]()
required_present_counts = list[list[int]]()


def parse_presents(present_sections: list[str]):
    global present_shapes
    for section in present_sections:
        index, shape = section.split(':\n')
        present_shapes.append(shape)

def parse_regions(regions_section: str):
    global regions, required_present_counts
    region_strings = [s.strip() for s in regions_section.split('\n')]
    for line in region_strings:
        size, present_counts = line.split(':')    
        width, length = size.split('x')
        regions.append((int(width.strip()), int(length.strip())))
        counts = [int(c.strip()) for c in present_counts.strip().split(' ')]
        required_present_counts.append(counts)


input = load_input()
def parse_input(input: str):
    sections = input.split('\n\n')
    present_sections = sections[:-1]
    areas_section = sections[-1]

    parse_presents(present_sections)
    parse_regions(areas_section)

parse_input(input)

test_shape_str = present_shapes[5]
test_shape = PresentShape(test_shape_str)

for v in test_shape.variants:
    print(v, '\n')



