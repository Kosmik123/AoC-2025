from helpers import load_input

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


distaneces = {}
for j in range(0, len(lines) - 1):
    for i in range(j, len(lines)):
        pass