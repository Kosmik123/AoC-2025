import sys
from helpers import load_input

required_lights_per_machine: list[set[int]] = []
buttons_per_machine: list[list[set[int]]] = []
joltages_per_machine: list[list[int]] = []
def parse_line(line: str):
    parse_lights(line) 
    parse_buttons(line)
    parse_joltages(line)


def parse_lights(line: str):
    global required_lights_per_machine
    lights_start = line.index('[') + 1
    lights_end = line.index(']')
    lights_section = line[lights_start:lights_end]
    lights = set[int]()
    for i in range(len(lights_section)):
        ch = lights_section[i]
        if ch == '#':
            lights.add(i)
    required_lights_per_machine.append(lights)           


def parse_buttons(line: str):
    global buttons_per_machine
    buttons_start = line.index(']') + 1
    buttons_end = line.index('{')
    buttons_section = line[buttons_start:buttons_end].strip()
    button_effects = buttons_section.split(' ')
    
    buttons: list[set[int]] = []
    for effect_str in button_effects:
        effect = parse_button(effect_str)
        buttons.append(effect)

    buttons_per_machine.append(buttons)


def parse_button(button_effect: str) -> set[int]:
    toggled_lights = set[int]() 
    start = button_effect.index('(') + 1
    end = button_effect.index(')')
    toggled_light_strings = button_effect[start:end].split(',')
    for light_str in toggled_light_strings:
        toggled_lights.add(int(light_str))
    return toggled_lights


def parse_joltages(line: str):
    global joltages_per_machine
    joltages_start = line.index('{') + 1
    joltages_end = line.index('}')
    joltage_strings = line[joltages_start:joltages_end].split(',')
    machine_joltages: list[int] = []
    for joltage_str in joltage_strings:
        machine_joltages.append(int(joltage_str))
    joltages_per_machine.append(machine_joltages)


input = '''
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
'''[1:-1]


input = load_input()
lines = input.split('\n')


for line in lines:
    parse_line(line)

assert len(required_lights_per_machine) == len(buttons_per_machine) == len(joltages_per_machine)
machine_count = len(buttons_per_machine)

# LIGHTS
def compare_sets(lhs: set, rhs: set) -> bool:
    for item in lhs:
        if not item in rhs: 
            return False
    for item in rhs:
        if not item in lhs: 
            return False
    return True


def apply_light_button_effect(effect: set[int], lights: set[int]):
    for light_index in effect:
        if light_index in lights:
            lights.remove(light_index)
        else:
            lights.add(light_index)


def test_light_button_presses(available_buttons: list[set[int]], requirement: set[int], pressed_buttons: set[int], starting_button: int, remaining_press_count: int):
    if remaining_press_count <= 0:
        testing_set = set[int]()
        for b in pressed_buttons:
            effect = available_buttons[b]
            apply_light_button_effect(effect, testing_set)
        #print ("Trying", pressed_buttons)
        return compare_sets(testing_set, requirement)
    
    for button in range(starting_button, len(available_buttons) - remaining_press_count + 1):
        pressed_buttons.add(button)
        if test_light_button_presses(available_buttons, requirement, pressed_buttons, button + 1, remaining_press_count - 1):
            return True    
        pressed_buttons.remove(button)
    
    return False


required_light_press_counts_per_machine: list[int] = [] 
for machine_index in range(machine_count):
    required_lights = required_lights_per_machine[machine_index]
    available_buttons = buttons_per_machine[machine_index]
    for presses_count in range(len(available_buttons) + 1):
        pressed_buttons = set[int]()
        if test_light_button_presses(available_buttons, required_lights, pressed_buttons, 0, presses_count):
            required_light_press_counts_per_machine.append(presses_count)
            break
    else:
        print("Couldn't find solution for machine:", machine_index)

print()
print("Need", sum(required_light_press_counts_per_machine), "presses to light up lights")
print()



# JOLTAGES
def compare_lists(lhs: list, rhs: list):
    if len(lhs) != len(rhs):
        return False
    for i in range(len(lhs)):
        if lhs[i] != rhs[i]:
            return False
    return True


def calculate_joltage_press_count(requirement: list[int], available_buttons: list[set[int]]) -> int:
    for potential_press_count in range(150):
        print("Trying", potential_press_count, "presses")
        button_presses = [0] * len(available_buttons)
        if test_joltage_button_presses(available_buttons, requirement, button_presses, 0, potential_press_count):
            return potential_press_count
    return None 


def apply_joltage_button_effect(effect: set[int], joltages: list[int]):
    for i in effect:
        joltages[i] += 1


def print_button_presses(presses: list[int]):
    print ("pressing buttons: ", end='')
    show_comma = False
    for i in range(len(presses)):
        if presses[i] <= 0:
            continue
        if show_comma:
            print(", ", end='')
        print(f"B({i}) x {presses[i]}", end='')
        show_comma = True
    print(" =", sum(presses))

def test_joltage_button_presses(available_buttons: list[set[int]], requirement: list[int], button_presses: list[int], starting_button: int, remaining_press_count: int):
    button_count = len(available_buttons)
    if remaining_press_count <= 0:
        test_list: list[int] = [0] * len(requirement) 
        for button_index in range(button_count):
            press_count = button_presses[button_index]
            if press_count <= 0:
                 continue
            effect = available_buttons[button_index]
            for _ in range(press_count):
                apply_joltage_button_effect(effect, test_list)

        #print ("Resulting joltages:", test_list)
        #print()

        if compare_lists(test_list, requirement):
            print_button_presses(button_presses)
            return True
        else: 
            return False

    for button_index in range(starting_button, button_count):
        button_presses[button_index] += 1
        if test_joltage_button_presses(available_buttons, requirement, button_presses, button_index, remaining_press_count - 1):
            return True
        button_presses[button_index] -= 1
    return False


required_joltage_press_counts_per_machine: list[int] = [] 
for machine_index in range(machine_count):
    required_joltages = joltages_per_machine[machine_index]
    available_buttons = buttons_per_machine[machine_index]
    print(f"For machine {machine_index} ", end='')
    count = calculate_joltage_press_count(required_joltages, available_buttons)
    if count == None:
        print("no solution!")
    required_joltage_press_counts_per_machine.append(count)

print()
print("Buttons need be pressed", sum(required_joltage_press_counts_per_machine), "times to set joltages")
print()


