from helpers import load_input

MAX_ROTATION = 100

counted_zeros = 0
passed_zeros = 0

def rotate(current: int, angle: int) -> int:
    global passed_zeros
    assert 0 <= current < MAX_ROTATION

    old = current
    current += angle 

    passed = abs(current // MAX_ROTATION)

    passed_zeros += passed

    print ("Rotate from", old, "to", current, ", passed zeros:", passed)

    current %= MAX_ROTATION
    if current < 0:
        current+= MAX_ROTATION
    return current

input = load_input()
current_rotation = 50

lines = input.split('\n')
for line in lines:
    direction = line[0]
    angle = int(line[1:])    
    if direction == 'L':
        angle *= -1
    
    current_rotation = rotate(current_rotation, angle)
    if current_rotation == 0:
        counted_zeros += 1

print(counted_zeros, passed_zeros, passed_zeros + counted_zeros)