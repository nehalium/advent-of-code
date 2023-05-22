from functools import reduce

from utils.filereader import FileReader

print('Hello, Day {day}!'.format(day=1))

lines = FileReader('input.txt').get_lines()

iteration = 0
count = 0
previous_line = 0

for line in lines:
    if iteration > 0:
        if previous_line < int(line):
            count += 1
    previous_line = int(line)
    iteration += 1

print('Part 1 Answer: {result}'.format(result=count))
