import statistics
from utils.filereader import FileReader

print('Hello, Day {day}!'.format(day=5))

data = FileReader('input.txt').get_lines()
positions = list(map(lambda x: int(x), data[0].split(',')))
median = statistics.median(positions)
fuel_spent = int(sum(list(map(lambda x: abs(x - median), positions))))

print('Part 1 Answer: {result}'.format(result=fuel_spent))
