from utils.filereader import FileReader

print('Hello, Day {day}!'.format(day=8))

lines = FileReader('input.txt').get_lines()
count = 0
for line in lines:
    line_parts = line.split('|')
    output_values = line_parts[1].strip().split()
    filtered_sizes = list(filter(lambda x: len(x) in [2, 3, 4, 7], output_values))
    count += len(filtered_sizes)

print('Part 1 Answer: {result}'.format(result=count))
