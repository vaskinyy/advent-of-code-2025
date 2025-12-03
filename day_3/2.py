from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()

lines = [[int(el) for el in item] for item in parser.get_input_lines()]

sequence_length = 12

max_numbers = []

len_lines = len(lines)
for i, line in enumerate(lines):
    print(f'{i+1}/{len_lines}')

    candidate = []

    start_index = 0
    for i in range(12):
        last_index = i - 11
        if last_index >= 0:
            last_index = len(line)
        item = max(line[start_index:last_index])
        start_index = line.index(item, start_index) + 1
        candidate.append(item)

    number = int(''.join([str(el) for el in candidate]))
    max_numbers.append(number)

print(max_numbers)
print(sum(max_numbers))
