from collections import defaultdict

from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()

lines = parser.get_input_lines()

ranges = []
for range_str in lines:
    if '-' in range_str:
        ranges.append((int(range_str.split('-')[0]), int(range_str.split('-')[1])))


initial_ranges = []
updated_ranges = sorted(ranges)

while initial_ranges != updated_ranges:
    initial_ranges = updated_ranges
    updated_ranges = []
    for left, right in initial_ranges:
        if not updated_ranges:
            updated_ranges.append((left, right))
            continue
        prev_left, prev_right = updated_ranges[-1]

        if left <= prev_right:
            updated_ranges[-1] = (prev_left, max(prev_right, right))
        else:
            updated_ranges.append((left, right))


print(updated_ranges)

print(sum(right - left + 1 for left, right in updated_ranges))