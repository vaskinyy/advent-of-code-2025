from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()

lines = [[int(el) for el in item] for item in parser.get_input_lines()]

max_numbers = []

for line in lines:
    cur_max = 0
    for i, item in enumerate(line):
        if len(line[i + 1:]) < 1:
            break
        new_max = int(f'{item}{max(line[i + 1:])}')
        if new_max > cur_max:
            cur_max = new_max
    max_numbers.append(cur_max)

print(max_numbers)
print(sum(max_numbers))
