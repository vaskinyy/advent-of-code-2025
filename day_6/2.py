import math
from collections import defaultdict
test_mode = False

if test_mode:
    with open('test_input.txt', 'r') as f:
        lines = [item for item in f.readlines()]
else:
    with open('full_input.txt', 'r') as f:
        lines = [item for item in f.readlines()]

split_lines = [line[:-1] if line.endswith('\n') else line for line in lines]

signs = split_lines[-1]
numbers = split_lines[:-1]

cur_sign = signs[0]
cur_numbers = []

numbers_signs = []

for i in range(len(signs)):
    if signs[i] == "*" or signs[i] == "+":
        cur_sign = signs[i]
    digits = [item[i] for item in numbers if item[i]]
    if set(digits) == set(' '):
        numbers_signs.append((cur_sign, cur_numbers))
        cur_numbers = []
    else:
        digits = [item for item in digits if item != ' ']
        cur_numbers.append(int(sum((int(digit) if digit != ' ' else 0) * math.pow(10, len(digits) - 1 - j) for j, digit in enumerate(digits))))

numbers_signs.append((cur_sign, cur_numbers))

results = []
for sign, numbers in numbers_signs:
    if sign == "*":
        results.append(math.prod(numbers))
    else:
        results.append(sum(numbers))

print(results)
print(sum(results))