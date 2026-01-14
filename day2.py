from helpers import load_input

def is_id_valid(id) -> bool:
    digits = str(id)
    halfway_index = len(digits) // 2
    for checked_length in range(1, halfway_index + 1):
        if len(digits) % checked_length != 0:
            continue

        checked_sequence = digits[0:checked_length]
        repeat_count = len(digits) // checked_length
        repeated_sequence = repeat_count * checked_sequence
        if repeated_sequence == digits:
            return False

    return True


def append_invalid_ids(start, end, invalid_ids_list: list):
    for id in range(start, end + 1):
        if not is_id_valid(id):
            invalid_ids_list.append(id)



input = '''11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124'''

input = load_input()

ranges = input.split(',')
all_invalid_ids = []
for id_range in ranges:
    parts = id_range.split('-')
    start = int(parts[0].strip())
    end = int(parts[1].strip())
    append_invalid_ids(start, end, all_invalid_ids)

print (all_invalid_ids)
invalid_ids_sum = sum(all_invalid_ids)
print(invalid_ids_sum)


