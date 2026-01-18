from helpers import load_input




def compare_sets(lhs, rhs) -> bool:
    for item in lhs:
        if not item in rhs: 
            return False
    for item in rhs:
        if not item in lhs: 
            return False
    return True



required_lights_per_machine: list[set[int]] = []
buttons_per_machine: list[list[set[int]]] = []

def parse_line(line: str):
    parse_lights(line) 
    parse_buttons(line)


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


def apply_button_effect(effect: set[int], lights: set[int]):
    for light_index in effect:
        if light_index in lights:
            lights.remove(light_index)
        else:
            lights.add(light_index)


def test_button_presses(available_buttons: list[set[int]], requirement: set[int], pressed_buttons: set[int], starting_button: int, remaining_presses: int):
    if remaining_presses <= 0:
        testing_set = set[int]()
        for b in pressed_buttons:
            effect = available_buttons[b]
            apply_button_effect(effect, testing_set)
        #print ("Trying", pressed_buttons)
        return compare_sets(testing_set, requirement)
    
    for button in range(starting_button, len(available_buttons) - remaining_presses + 1):
        pressed_buttons.add(button)
        if test_button_presses(available_buttons, requirement, pressed_buttons, button + 1, remaining_presses - 1):
            return True    
        pressed_buttons.remove(button)
    
    return False







input = '''
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
'''[1:-1]


input = load_input()
lines = input.split('\n')


for line in lines:
    parse_line(line)

assert len(required_lights_per_machine) == len(buttons_per_machine)



required_press_counts_per_machine: list[int] = [] 

for machine_index in range(len(required_lights_per_machine)):
    required_lights = required_lights_per_machine[machine_index]
    available_buttons = buttons_per_machine[machine_index]
    for presses_count in range(len(available_buttons) + 1):
        pressed_buttons = set[int]()
        if test_button_presses(available_buttons, required_lights, pressed_buttons, 0, presses_count):
            required_press_counts_per_machine.append(presses_count)
            break
    else:
        print("Couldn't find solution for machine:", machine_index)

print()
print("Answer:", sum(required_press_counts_per_machine))