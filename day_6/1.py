from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()

lines = parser.get_input_lines()

split_lines = [line.split(' ') for line in lines]
cleaned_lines = [[item for item in line if item] for line in split_lines]

signs = cleaned_lines[-1]
numbers = cleaned_lines[:-1]


results = []
for i in range(len(cleaned_lines[0])):
    result = -1
    for line in numbers:
        sign = signs[i]
        if result == -1:
            result = int(line[i])
            continue
        if sign == '+':
            result += int(line[i])
        else:
            result *= int(line[i])
    results.append(result)

print(results)
print(sum(results))