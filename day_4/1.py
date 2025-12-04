from models.board import get_coords_around
from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()

parser.build_boards()


board = parser.get_board()
items = board.items
width = board.width
height = board.height



num_items = 0


for i in range(height):
    for j in range(width):
        if items[i][j] != "@":
            continue
        coords = get_coords_around(i, j, height, width)
        counter = 0
        for near_i, near_j in coords:
            if items[near_i][near_j] == "@":
                counter += 1
        if counter < 4:
            num_items += 1

print(num_items)