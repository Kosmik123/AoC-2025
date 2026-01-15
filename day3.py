from helpers import load_input


def get_max_digit(bank: str, start: int, end: int) -> tuple[int, int]:    
    assert 0 <= start < len(bank)
    assert start <= end < len(bank)
    
    max_value = 0
    max_value_index = None
    for index in range(start, end + 1):
        value = int(bank[index])
        if max_value_index == None or value > max_value:
            max_value = value
            max_value_index = index 

    return max_value, max_value_index        


def get_max_joltage(bank: str, requested_count: int = 2) -> int:
    assert len(bank) >= requested_count

    bateries = []
    previous_digit_index = -1
    for index in range(requested_count):
        remaining_count = requested_count - len(bateries)
        last_possible_position_in_bank = len(bank) - remaining_count
        value, index_in_bank = get_max_digit(bank, previous_digit_index + 1, last_possible_position_in_bank)
        bateries.append(str(value))
        previous_digit_index = index_in_bank

    return int(''.join(bateries))


input = '''987654321111111
811111111111119
234234234234278
818181911112111'''

input = load_input()

lines = input.split('\n')
total_joltage = 0
for line in lines:
    joltage = get_max_joltage(line, 12)
    total_joltage += joltage

print(total_joltage)