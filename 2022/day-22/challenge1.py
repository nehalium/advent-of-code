from utils.filereader import FileReader

print('Hello, Day {day}!'.format(day=22))

lines = FileReader('test.txt').get_lines()

for line in lines:
    print(line)

print('Part 1 Answer: {result}'.format(result=0))
