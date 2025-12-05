from collections import defaultdict

from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()

lines = parser.get_input_lines()

ranges = []
ingredient_ids = []
collecting_ingredients = False
for range_str in lines:
    if '-' in range_str:
        ranges.append((int(range_str.split('-')[0]), int(range_str.split('-')[1])))
    else:
        ingredient_ids.append(int(range_str))




fresh_ids = []

for item in ingredient_ids:
    for left, right in ranges:
        if left <= item <= right:
            fresh_ids.append(item)
            break


print(fresh_ids)
print(len(fresh_ids))
