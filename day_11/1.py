from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()

paths = {}
for line in parser.get_input_lines():
    splits = line.split(' ')
    paths[splits[0][:-1]] = splits[1:]
print(paths)

queue = ['you']

counter = 0

while queue:
    cur = queue.pop(0)
    if cur == 'out':
        counter += 1
        continue
    for next in paths[cur]:
        queue.append(next)

print(counter)