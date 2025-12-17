from itertools import combinations

import shapely

from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()

lines = [line.split(',') for line in parser.get_input_lines()]
coords = [(int(i), int(j)) for i, j in lines]

coord_set = set(coords)

pairs = [(coord1, coord2) for coord1, coord2 in combinations(coords, 2)]

areas = []

max_area = 0

red_green = shapely.Polygon([(x, y) for (y, x) in lines])

for coord1, coord2 in pairs:
    ax = coord1[1]
    ay = coord1[0]
    bx = coord2[1]
    by = coord2[0]

    left = ax if ax < bx else bx
    right = ax if ax > bx else bx
    top = ay if ay < by else by
    bottom = ay if ay > by else by

    candidate = shapely.box(left, top, right, bottom)

    if not shapely.contains(red_green, candidate):
        continue

    area = (right - left + 1) * (bottom - top + 1)
    areas.append(area)

print(max(areas))