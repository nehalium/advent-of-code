from functools import reduce

from utils.filereader import FileReader


def get_common_character(first, second):
    return next(iter(set(first) & set(second)))


def get_priority(character):
    codepoint = ord(character)
    if codepoint >= 97:
        return codepoint - 96  # a - z
    else:
        return codepoint - 38  # A - Z


print('Hello, Day {day}!'.format(day=3))

lines = FileReader('input.txt').get_lines()

items = []
total = 0

for line in lines:
    first_compartment = line[0: int(len(line) / 2)]
    second_compartment = line[int(len(line) / 2):]
    items.append(get_common_character(first_compartment, second_compartment))

total = reduce((lambda x, y: x + y), map(get_priority, items))

print('Part 1 Answer: {result}'.format(result=total))
