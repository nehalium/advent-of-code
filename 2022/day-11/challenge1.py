from utils.filereader import FileReader
from monkey import Monkey

print('Hello, Day {day}!'.format(day=11))

lines = FileReader('input.txt').get_lines()

line_index = 1
monkey = None
monkeys = {}
inspected_counts = []
total = 0

for line in lines:
    if Monkey.is_new_monkey(line):  # start a new monkey
        line_index = 1
        monkey = Monkey(line)
    if line_index == 1:  # first line already read
        line_index += 1
    elif 1 < line_index < 6:  # read lines 2-5
        monkey.extract(line_index, line)
        line_index += 1
    elif line_index == 6:  # read line 6 and done
        monkey.extract(line_index, line)
        monkeys[monkey.index] = monkey
        line_index = 0

for i in range(20):
    for index, monkey in monkeys.items():
        monkey.inspect_items(monkeys)

inspected_counts = list(map((lambda x: x.inspected_count), monkeys.values()))
inspected_counts.sort()
inspected_counts.reverse()
total = inspected_counts[0] * inspected_counts[1]

print('Part 1 Answer: {result}'.format(result=total))
