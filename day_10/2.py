from collections import defaultdict

from parsers.input_parser import InputParser
import z3

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
    cur_indicator = cur_indicators[0]

    solver = z3.Optimize()
    button_states = z3.IntVector("button_states", len(cur_buttons))
    button_indices = defaultdict(list)
    for i, cur_button in enumerate(cur_buttons):
        solver.add(button_states[i] >= 0)
        for j in cur_button:
            button_indices[j].append(i)

    for i, idxes in button_indices.items():
        solver.add(cur_indicator[i] == sum(button_states[j] for j in idxes))

    presses = z3.Sum(button_states)
    solver.minimize(presses)
    solver.check()
    sums.append(solver.model().eval(presses).as_long())

print(sums)
print(sum(sums))

