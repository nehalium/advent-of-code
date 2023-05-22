from functools import reduce

from utils.filereader import FileReader

print('Hello, Day {day}!'.format(day=1))

lines = FileReader('input.txt').get_lines()

values = []
subvalues = []
sums = []
total = 0

# listify the input
for line in lines:
    if line != "\n":
        subvalues.append(int(line))
    else:
        values.append(subvalues)
        subvalues = []
values.append(subvalues)

# sum up the sub lists
for v in values:
    sums.append(reduce((lambda x, y: x + y), v))

# order the resulting list
sums.sort(reverse=True)

# filter for top three
sums = [sums[i] for i in [0, 1, 2]]

# sum up the result
total = reduce((lambda x, y: x + y), sums)

print('Part 2 Answer: {result}'.format(result=total))
