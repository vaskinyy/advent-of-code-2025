import math
from itertools import combinations

from parsers.input_parser import InputParser

test_mode = False

number_of_connections = 10
if not test_mode:
    number_of_connections = 1000

parser = InputParser(test_mode)
parser.parse()

coords = [[int(el) for el in item.split(',')] for item in parser.get_input_lines()]

pair_distances = [(item1, item2, math.dist(item1, item2)) for (item1, item2) in combinations(coords, 2)]


item_circuit = {tuple(item1): set([tuple(item1)]) for item1 in coords}

sorted_distances = sorted(pair_distances, key=lambda x: x[2] )

for item1, item2, distance in sorted_distances[:number_of_connections]:
    new_circuit = item_circuit[tuple(item1)].union(item_circuit[tuple(item2)])
    for item in new_circuit:
        item_circuit[tuple(item)] = new_circuit

keys = list(item_circuit.keys())

for key in keys:
    if key not in item_circuit:
        continue
    elements = item_circuit[key]
    for el in elements:
        if el != key:
            del item_circuit[el]

sorted_lengths = sorted([len(item_circuit[item]) for item in item_circuit], reverse=True)
first_tree = sorted_lengths[:3]
print(math.prod(first_tree))