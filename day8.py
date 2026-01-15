import math
from helpers import load_input

def sqr_distance(lhs: tuple[int, int, int], rhs: tuple[int, int, int]) -> int:
    x_diff = lhs[0] - rhs[0]
    y_diff = lhs[1] - rhs[1]
    z_diff = lhs[2] - rhs[2]
    return x_diff ** 2 + y_diff ** 2 + z_diff ** 2

def distance(lhs: tuple[int, int, int], rhs: tuple[int, int, int]) -> float:
    return math.sqrt(sqr_distance(lhs, rhs))


input = '''
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
'''[1:-1]



#input = load_input()
lines = input.split('\n')

points = []
for line in lines:
    x_str, y_str, z_str = line.split(',')
    point = (int(x_str), int(y_str), int(z_str))
    points.append(point)

print(points)


sqr_distances = {}
for i in range(0, len(lines) - 1):
    point1 = points[i]
    for j in range(i + 1, len(lines)):
        point2 = points[j]
        sqr_distances[(i, j)] = sqr_distance(point1, point2)

for elem in sqr_distances.items():
    print(elem)
    