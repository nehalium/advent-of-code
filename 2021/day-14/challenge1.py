from utils.filereader import FileReader

print('Hello, Day {day}!'.format(day=14))

lines = FileReader('test.txt').get_lines()

for line in lines:
    pass

print('Part 1 Answer: {result}'.format(result=0))