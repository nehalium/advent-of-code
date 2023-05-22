from functools import reduce

from utils.filereader import FileReader


def chunk_list(input_list, chunk_size):
    return [input_list[i:i+chunk_size] for i in range(0, len(input_list), chunk_size)]


def get_common_character(lists):
    return next(iter((set(lists[0]) & set(lists[1]) & set(lists[2]))))


def get_priority(character):
    codepoint = ord(character)
    if codepoint >= 97:
        return codepoint - 96  # a - z
    else:
        return codepoint - 38  # A - Z


print('Hello, Day {day}!'.format(day=3))

lines = FileReader('input.txt').get_lines()

items = []
common_characters = []
total = 0

for line in lines:
    items.append(line.strip('\n'))

common_characters = list(map(get_common_character, chunk_list(items, 3)))
total = reduce((lambda x, y: x + y), map(get_priority, common_characters))

print('Part 2 Answer: {result}'.format(result=total))
