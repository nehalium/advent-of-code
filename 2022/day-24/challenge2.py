from utils.filereader import FileReader

print('Hello, Day {day}!'.format(day=24))

lines = FileReader('test.txt').get_lines()

for line in lines:
    print(line)

print('Part 2 Answer: {result}'.format(result=0))
