from utils.filereader import FileReader


def get_marker_index(data_stream, marker_length):
    for i in range(0, len(data_stream) - marker_length):
        subset = line[i:i+marker_length]
        if len(set(subset)) == len(subset):
            return i + marker_length


print('Hello, Day {day}!'.format(day=6))

lines = FileReader('input.txt').get_lines()

marker_indices = []

for line in lines:
    marker_indices.append(get_marker_index(line, 14))

print('Part 2 Answer: {result}'.format(result=marker_indices))
