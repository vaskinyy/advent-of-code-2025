from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()

lines = [line.split(' ') for line in parser.get_input_lines()]

lights = []
buttons = []
indicators = []

for i, line in enumerate(lines):
    lights.append([])
    buttons.append([])
    indicators.append([])
    for item in line:
        if item.startswith('['):
            lights[i].append(item[1:-1])
        elif item.startswith('('):
            cleaned_items = [int(el) for el in item[1:-1].split(',')]
            buttons[i].append(cleaned_items)
        elif item.startswith('{'):
            cleaned_items = [int(el) for el in item[1:-1].split(',')]
            indicators[i].append(cleaned_items)

sums = []
for cur_lights, cur_buttons, cur_indicators in zip(lights, buttons, indicators):
    target_light = cur_lights[0]

    queue = [('.'*len(target_light), i, tuple([0 for i in range(len(cur_buttons))])) for i in range(len(cur_buttons))]
    visited = set()

    while queue:
        light, index, buttons_state = queue.pop(0)

        light = list(light)
        for i in cur_buttons[index]:
            light[i] = '.' if light[i] == '#' else '#'
        light = ''.join(light)

        new_buttons_state = tuple(
            [buttons_state[i] if i != index else buttons_state[i] + 1 for i in range(len(buttons_state))])
        if light == target_light:
            sums.append(sum(new_buttons_state))
            print(new_buttons_state)
            break


        if new_buttons_state in visited:
            continue

        for i in range(len(cur_buttons)):
            queue.append((light, i, new_buttons_state))


print(sums)
print(sum(sums))

