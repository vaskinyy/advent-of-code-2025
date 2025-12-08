from collections import defaultdict

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

locations = defaultdict(int)

locations[start_pos[1]] = 1


for i in range(board.height):
    for j in range(board.width):
        if board.items[i][j] == "^" and locations[j] > 0:
            locations[j - 1] += locations[j]
            locations[j + 1] += locations[j]
            locations[j] = 0


print(sum(locations.values()))
