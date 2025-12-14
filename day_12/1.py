from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()

lines = parser.get_input_lines()

forms_sums = {}
cur_number = 0

board_lines = []
present_coords = []
boards = []

for line in lines:
    if len(line) == 2:
        if not board_lines:
            continue
        forms_sums[cur_number] = present_coords
        cur_number += 1
        board_lines = []
        present_coords = []

    if '.' in line or '#' in line:
        board_lines.append([item for item in line])
        for item in line:
            if item == '#':
                present_coords.append(1)
    elif 'x' in line:
        sizes = []
        shapes = []
        board_splits = line.split(' ')
        for item in board_splits:
            if 'x' in item:
                sizes.append(int(item.split('x')[0]))
                sizes.append(int(item[:-1].split('x')[1]))
            else:
                shapes.append(int(item))
        boards.append((sizes, shapes))

forms_sums[cur_number] = present_coords

counts = 0
for boards in boards:
    ((width, height), quantities) = boards
    presents_for_region = []
    for i, quantity in enumerate(quantities):
        if quantity == 0:
            continue
        for _ in range(quantity):
            presents_for_region.append(forms_sums[i])

    presents_for_region_length = sum(len(tile) for tile in presents_for_region)
    counts += 1 if presents_for_region_length < width * height else 0
print(counts)
