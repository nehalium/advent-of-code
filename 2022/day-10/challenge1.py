from utils.filereader import FileReader

print('Hello, Day {day}!'.format(day=10))

lines = FileReader('input.txt').get_lines()

x = 1
ops = [0]
cycle_num = 1
signal_strength = {}
total = 0

for line in lines:
    parts = line.strip("\n").split(" ")
    if parts[0] == "noop":
        ops += [0]
    elif parts[0] == "addx":
        ops += [0]
        ops += [int(parts[1])]

while len(ops) > 0:
    x += ops.pop(0)
    signal_strength[cycle_num] = cycle_num * x
    cycle_num += 1

total = sum([signal_strength[20],
             signal_strength[60],
             signal_strength[100],
             signal_strength[140],
             signal_strength[180],
             signal_strength[220]])

print('Part 1 Answer: {result}'.format(result=total))
