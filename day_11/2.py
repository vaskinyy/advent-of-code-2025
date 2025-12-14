from functools import cache

from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()

paths = {}
for line in parser.get_input_lines():
    splits = line.split(' ')
    paths[splits[0][:-1]] = splits[1:]
print(paths)

@cache
def find_paths(cur, target):
    return 1 if cur == target else sum(find_paths(item, target) for item in paths.get(cur, []))

total = find_paths("svr", "fft") * find_paths("fft", "dac") * find_paths("dac", "out")
print(total)
