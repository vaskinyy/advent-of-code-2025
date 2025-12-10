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


def coords_to_fill(coord1, coord2, existing_coords):
    x1, y1 = coord1
    x2, y2 = coord2

    if x1 == x2:
        lower, upper = sorted((y1, y2))
        return {(x1, y) for y in range(lower + 1, upper)}

    if y1 == y2:
        left, right = sorted((x1, x2))
        return {(x, y1) for x in range(left + 1, right)}

    other_corners = [(x1, y2), (x2, y1)]
    if not all(corner in existing_coords for corner in other_corners):
        return set()

    x_start, x_end = sorted((x1, x2))
    y_start, y_end = sorted((y1, y2))

    if x_end - x_start <= 1 or y_end - y_start <= 1:
        return set()

    return {
        (x, y)
        for x in range(x_start + 1, x_end)
        for y in range(y_start + 1, y_end)
    }


for coord1, coord2 in pairs:
    to_fill = coords_to_fill(coord1, coord2, coord_set)
    if not to_fill:
        continue

    if any(point in coord_set for point in to_fill):
        continue

    # print((coord1[1], coord1[0]), (coord2[1], coord2[0]))
    print(coord1, coord2)
    coord_set.update(to_fill)
    areas.append(abs(coord1[0] - coord2[0] + 1) * abs(coord1[1] - coord2[1] + 1))

print(sorted(areas))
