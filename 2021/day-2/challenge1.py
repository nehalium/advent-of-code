from utils.filereader import FileReader

print('Hello, Day {day}!'.format(day=2))

lines = FileReader('input.txt').get_lines()

horizontal = 0
depth = 0

for line in lines:
    line_parts = line.split(' ')
    direction = line_parts[0]
    distance = int(line_parts[1])
    if direction == 'forward':
        horizontal += distance
    if direction == 'down':
        depth += distance
    if direction == 'up':
        depth -= distance

print('Part 1 Answer: {result}'.format(result=(horizontal * depth)))
