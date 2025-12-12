import math
from collections import deque, defaultdict
from heapq import heappop, heappush

from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()


def has_cycle(items, start_key):
    if start_key == 'svr' or start_key == 'out':
        return False

    queue = [start_key]

    while queue:
        item = queue.pop(0)
        if item in ['svr', 'out']:
            return False
        if item == start_key:
            return True

        for next in items[item]:
            queue.append(next)

    return False


paths = {}
for line in parser.get_input_lines():
    splits = line.split(' ')
    paths[splits[0][:-1]] = splits[1:]
print(paths)

device_map = paths
ranks = {}
rank_stack = deque([("svr", 0)])
while len(rank_stack):
  key, rank = rank_stack.popleft()

  if key in ranks and ranks[key] == rank:
    continue

  ranks[key] = rank

  if key not in device_map:
    continue

  for conn in device_map[key]:
    rank_stack.append((conn, rank + 1))


def count_paths(start, end, count):
  counts = defaultdict(int)
  done = set()
  stack = [(ranks[start], start)]
  counts[start] = count

  while len(stack):
    _, key = heappop(stack)

    if key not in device_map:
      continue

    conns = device_map[key]
    for conn in conns:
      counts[conn] += counts[key]
      if conn not in done:
        heappush(stack, (ranks[conn], conn))
        done.add(conn)

  return counts[end]

p1 = count_paths("svr", "fft", 1)
p2 = count_paths("fft", "dac", p1)
p3 = count_paths("dac", "out", p2)
print(p3)

# while True:
#     has_loops = False
#     keys = list(paths.keys())
#     for key in keys:
#         if has_cycle(paths, key):
#             has_loops = True
#             for cur_key in paths:
#                 items = paths[cur_key]
#                 if key in items:
#                     items.remove(key)
#             paths.pop(key)
#             break
#     if not has_loops:
#         break

collected_visited = set()

def calculate_num_paths(start, finish, visited):

    queue = [start]

    counter = 0

    while queue:
        cur = queue.pop(0)
        # print(len(queue))
        if cur == finish:
            counter += 1
            continue

        if cur in visited or cur == 'out':
            continue

        visited.add(cur)

        for next in paths[cur]:
            queue.append(next)
    return counter, visited




collected_counters = []
counter, collected_visited = calculate_num_paths('svr', 'fft', collected_visited)

collected_counters.append(counter)
collected_visited = set()
print(counter)
counter, collected_visited = calculate_num_paths('fft', 'dac', collected_visited)
collected_counters.append(counter)
print(counter)
collected_visited = set()
counter, collected_visited = calculate_num_paths('dac', 'out', collected_visited)

collected_counters.append(counter)
print(counter)

print(math.prod(collected_counters))

