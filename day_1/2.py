from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()

rotation_pairs = [(item[0], int(item[1:])) for item in parser.get_input_lines()]

print(rotation_pairs)

position = 50

zero_counts = 0

for direction, clicks in rotation_pairs:
    for i in range(clicks):

        if direction == 'R':
            position += 1
            if position == 100:
                position = 0
        else:
            position -= 1
            if position == -1:
                position = 99

        if position == 0:
            zero_counts += 1

    # print(position)
print(zero_counts)