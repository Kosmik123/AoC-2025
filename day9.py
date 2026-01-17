from helpers import load_input, Point

green_tiles: set[Point] = {}
invalid_tiles: set[Point] = {}
def is_green(point: Point) -> bool:
    global green_tiles, invalid_tiles
    if point in green_tiles:
        return True
    if point in invalid_tiles:
        return False

    #calculationlogic
    green = True
    if green:
        green_tiles.add(point)
    else:
        invalid_tiles.add(point)
    return green


def calculate_area(tile1: tuple[int, int], tile2: tuple[int, int]):
    width = abs(tile1.x - tile2.x) + 1
    length = abs(tile1.y - tile2.y) + 1
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

red_tiles: list[Point] = []

indices_by_x: dict[int, list[int]] = {}
indices_by_y: dict[int, list[int]] = {}

def register_tile(index: int, x: int, y: int):
    global indices_by_x, indices_by_y
    if x not in indices_by_x:
        indices_by_x[x] = []
    if y not in indices_by_y:
        indices_by_y[y] = []
    indices_by_x[x].append(index)
    indices_by_y[y].append(index)


min_x = None
max_x = None
min_y = None
max_y = None

for i in range(len(lines)):
    line = lines[i]
    x_str, y_str = line.split(',')
    point = Point(int(x_str), int(y_str))
    if min_y == None or point.y < min_y:
        min_y = point.y
    if max_y == None or point.y > max_y:
        max_y = point.y
    if min_x == None or point.x < min_x:
        min_x = point.x
    if max_x == None or point.x > max_x:
        max_x = point.x

    register_tile(i, x_str, y_str)
    red_tiles.append(point)


areas_by_tiles: dict[tuple[int, int], int] = {}
for i in range(len(red_tiles) - 1):
    tile1 = red_tiles[i]
    for j in range(i + 1, len(red_tiles)):
        tile2 = red_tiles[j]         
        area = calculate_area(tile1, tile2)
        areas_by_tiles[(i, j)] = area


class TilesAndArea:
    def __init__(self, tiles: tuple[int, int], area: int):
        self.tiles = tiles
        self.area = area

    def get_area(self):
        return self.area
    
    def __str__(self):
        return f"{self.tiles}: {self.area}"

sorted_list_of_areas_and_tiles: list[TilesAndArea] = []
for tiles, area in areas_by_tiles.items():
    sorted_list_of_areas_and_tiles.append(TilesAndArea(tiles, area))
sorted_list_of_areas_and_tiles.sort(reverse=True, key=TilesAndArea.get_area)

highest = sorted_list_of_areas_and_tiles[0]
print(highest.area, "is between tiles", highest.tiles)

class Rect:
    def __init__(self, point1: Point, point2:  Point):
        self.x_min = min(point1.x, point2.x)
        self.x_max = max(point1.x, point2.x)
        self.y_min = min(point1.y, point2.y)
        self.y_max = max(point1.y, point2.y)

    def has_inside(self, point: Point) -> bool:
        return self.x_min < point.x < self.x_max and self.y_min < point.y < self.y_max
    
    def has_on_edge(self, point: Point) -> bool:
        if self.x_min < point.x < self.x_max:
            return point.y == self.y_min or point.y == self.y_max
        elif self.y_min < point.y < self.y_max:
            return point.x == self.x_min or point.x == self.x_max 
        return False

    def check_line_intersect(self, line_start: Point, line_end: Point) -> bool:
        line = (line_start, line_end)
        if line_start.x == line_end.x: # vertical  
            return Rect.check_lines_intersection(line, (Point(self.x_min, self.y_min), Point(self.x_max, self.y_min))) or Rect.check_lines_intersection(line, (Point(self.x_min, self.y_max), Point(self.x_max, self.y_max)))
        elif line_start.y == line_end.y: # horizontal
            return Rect.check_lines_intersection(line, (Point(self.x_min, self.y_min), Point(self.x_min, self.y_max))) or Rect.check_lines_intersection(line, (Point(self.x_max, self.y_min), Point(self.x_max, self.y_max)))
        else:
            raise Exception() # invalid line
            

    def check_lines_intersection(line1: tuple[Point, Point], line2: tuple[Point, Point]):
        p1, p2 = line1
        p3, p4 = line2

        x1, x2 = sorted([p1.x, p2.x])
        y1, y2 = sorted([p1.y, p2.y])
        x3, x4 = sorted([p3.x, p4.x])
        y3, y4 = sorted([p3.y, p4.y])

        seg1_horizontal = y1 == y2
        seg2_horizontal = y3 == y4
        if seg1_horizontal and not seg2_horizontal:
            return x1 < x3 < x2 and y3 < y1 < y4

        if not seg1_horizontal and seg2_horizontal:
            return x3 < x1 < x4 and y1 < y3 < y2

        # Horizontal × Horizontal
        if seg1_horizontal and seg2_horizontal:
            return y1 == y3 and not (x2 < x3 or x4 < x1)

        # Vertical × Vertical
        return x1 == x3 and not (y2 < y3 or y4 < y1)



def contains_red_tile_inside(rect: Rect) -> bool:
    global red_tiles    
    for t in red_tiles:
        if rect.has_inside(t):
            return True
    return False


def is_instersected_with_green_line(rect: Rect) -> bool:
    global red_tiles
    for i in range(len(red_tiles)):
        next = (i + 1) % len(red_tiles)
        start = red_tiles[i]
        end = red_tiles[next]
        if rect.check_line_intersect(start, end):
            return True
    return False


def is_green_inside(rect: Rect) -> bool:
    global red_tiles
    center = Point(rect.x_max + rect.x_min // 2, rect.y_max + rect.y_min // 2)
    for i in range(len(red_tiles)):
        next = (i + 1) % len(red_tiles)
        start = red_tiles[i]
        end = red_tiles[next]



def is_rect_valid(tiles_and_area: TilesAndArea) -> bool:
    global red_tiles
    idx1, idx2 = tiles_and_area.tiles
    tile1 = red_tiles[idx1]
    tile2 = red_tiles[idx2]
    rect = Rect(tile1, tile2)
    if contains_red_tile_inside(rect):
        return False
        
    if is_instersected_with_green_line(rect):
        return False
    
    return True

for tiles_and_area in sorted_list_of_areas_and_tiles:
    if is_rect_valid(tiles_and_area):
        print ("Valid:", tiles_and_area)
        break
else:
    print("No good")       

drawing = ""    
