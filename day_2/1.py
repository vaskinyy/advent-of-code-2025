from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()

ranges = [(int(item.split('-')[0]), int(item.split('-')[1])) for item in parser.get_input_lines()[0].split(',')]

invalid_items = []

for left, right in ranges:
    if left > right:
        print("Invalid range TT")
        continue

    for item in range(left, right + 1):
        item_str = str(item)
        item_len = len(item_str)
        if item_len % 2 != 0:
            continue

        if item_str[:item_len//2] == item_str[item_len//2:]:
            invalid_items.append(item)

print(invalid_items)
print(sum(invalid_items))
