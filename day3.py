from helpers import load_input


def get_max_digit(bank: str, start: int, end: int) -> tuple[int, int]:
    
    assert 0 <= start < len(bank)
    assert start < end <= len(bank)
    
    max_value = 0
    max_value_index = None
    for index in range(start, end):
        value = int(bank[index])
        if max_value_index == None or value > max_value:
            max_value = value
            max_value_index = index 

    return max_value, max_value_index        


def get_max_joltage(bank: str) -> int:
    assert len(bank) > 1
    first, first_index = get_max_digit(bank, 0, len(bank) - 1)
    second, second_index = get_max_digit(bank, first_index + 1, len(bank))
    return int(str(first) + str(second))


input = '''987654321111111
811111111111119
234234234234278
818181911112111'''

input = load_input()

lines = input.split('\n')
total_joltage = 0
for line in lines:
    joltage = get_max_joltage(line)
    total_joltage += joltage

print(total_joltage)