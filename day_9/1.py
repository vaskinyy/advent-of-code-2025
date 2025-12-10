from itertools import combinations

from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()

lines = [line.split(',') for line in parser.get_input_lines()]
coords = [(int(i), int(j)) for i, j in lines]

coord_set = set(coords)

pairs = [(coord1, coord2) for coord1, coord2 in combinations(coords, 2)]

areas = []

for coord1, coord2 in pairs:
        areas.append(abs(coord1[0] - coord2[0] + 1) * abs(coord1[1] - coord2[1] + 1))

print(sorted(areas))
