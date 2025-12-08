from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()

parser.build_boards()

board = parser.get_board()

for i in range(board.height):
    for j in range(board.width):
        if board.items[i][j] == "S":
            start_pos = (i, j)
            break

locations = [start_pos]

visited_splits = set()

while locations:
    (i, j) = locations.pop()

    if i + 1 == board.height:
        continue

    next_location = (i + 1, j)

    if next_location in visited_splits:
        continue

    if board.items[next_location[0]][next_location[1]] == "^":
        visited_splits.add(next_location)
        locations.append((i + 1, j - 1))
        locations.append((i + 1, j + 1))
    else:
        locations.append(next_location)

print(len(visited_splits))