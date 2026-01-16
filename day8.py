import math
from helpers import load_input, add_distinct

class JunctionssDistance:
    def __init__(self, junction1_index: int, junction2_index: int, value: float):
        self.lower_index = min(junction1_index, junction2_index)
        self.higher_index = max(junction1_index, junction2_index)
        self.value = value

    def __str__(self):
        return f'[({self.lower_index}, {self.higher_index})] => {self.value}'

def sqr_distance(lhs: tuple[int, int, int], rhs: tuple[int, int, int]) -> int:
    x_diff = lhs[0] - rhs[0]
    y_diff = lhs[1] - rhs[1]
    z_diff = lhs[2] - rhs[2]
    return x_diff ** 2 + y_diff ** 2 + z_diff ** 2

def distance(lhs: tuple[int, int, int], rhs: tuple[int, int, int]) -> float:
    return math.sqrt(sqr_distance(lhs, rhs))


def get_value_from_junctions_distance(e: JunctionssDistance):
    return e.value


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

junctions = []
for line in lines:
    x_str, y_str, z_str = line.split(',')
    pair = (int(x_str), int(y_str), int(z_str))
    junctions.append(pair)

print(junctions)

sqr_distances = {}
for i in range(0, len(lines) - 1):
    junction1 = junctions[i]
    for j in range(i + 1, len(lines)):
        junction2 = junctions[j]
        sqr_distances[(i, j)] = sqr_distance(junction1, junction2)

junction_pairs_sorted_by_distance: list[JunctionssDistance] = []
for junction_pair, sqr_dist in sqr_distances.items():
    junctions_distance = JunctionssDistance(junction_pair[0], junction_pair[1], sqr_dist)
    junction_pairs_sorted_by_distance.append(junctions_distance)
junction_pairs_sorted_by_distance.sort(key=get_value_from_junctions_distance)

for pair in junction_pairs_sorted_by_distance:
    print(pair)


circuits: list[list[int]] = []
def are_points_connected(point1_index: int, point2_index: int) -> bool:
    global circuits
    for circuit in circuits:
        if point1_index in circuit and point2_index in circuit:
            return True
    return False

def get_circuit_index(junction_index: int) -> int:
    global circuits
    for i in range(len(circuits)):
        if junction_index in circuits[i]:
            return i
    return -1


step = 0
for pair in junction_pairs_sorted_by_distance:
    step += 1
    if step > 10:
        break
    
    if are_points_connected(pair.lower_index, pair.higher_index):
        continue
    
    circuit1_index = get_circuit_index(pair.lower_index)
    circuit2_index = get_circuit_index(pair.higher_index)

    if circuit1_index < 0 and circuit2_index < 0:
        new_circuit = []
        new_circuit.append(pair.lower_index)
        new_circuit.append(pair.higher_index)
        circuits.append(new_circuit)
    elif circuit1_index < 0 and circuit2_index >= 0:
        circuits[circuit2_index].append(pair.lower_index)
    elif circuit1_index >= 0 and circuit2_index < 0:
        circuits[circuit1_index].append(pair.higher_index)
    else: # both exist
        circuit1 = circuits.pop(circuit1_index)
        circuit2 = circuits.pop(circuit2_index)
        merged_circuit = circuit1 + circuit2
        circuits.append(merged_circuit)

    print(step, circuits)

circuits.sort(key=len, reverse=True)
print("sorted", circuits)