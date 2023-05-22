from functools import reduce

from utils.filereader import FileReader

print('Hello, Day {day}!'.format(day=9))


def get_data(lines_to_process):
    data_list = list()
    for line in lines_to_process:
        data_list.append(list(map(lambda x: int(x), list(line.strip()))))
    return data_list


def create_basin_map(number_of_rows, number_of_columns):
    return [[0] * number_of_columns for i in range(number_of_rows)]


def get_basin_iterator(basin_map_to_eval, row_index, column_index, i):
    if row_index > 0 and basin_map_to_eval[row_index - 1][column_index] > 0:
        return basin_map_to_eval[row_index - 1][column_index]
    if column_index > 0 and basin_map_to_eval[row_index][column_index - 1] > 0:
        return basin_map_to_eval[row_index][column_index - 1]
    if column_index < len(basin_map_to_eval[row_index]) - 1 and basin_map_to_eval[row_index][column_index + 1] > 0:
        return basin_map_to_eval[row_index][column_index + 1]
    if row_index < len(basin_map_to_eval) - 1 and basin_map_to_eval[row_index + 1][column_index] > 0:
        return basin_map_to_eval[row_index + 1][column_index]
    return i


def update_basin_map(basin_map_to_eval):
    for row_index in range(0, len(basin_map_to_eval)):
        for column_index in range(0, len(basin_map_to_eval[row])):
            if row_index > 0 and \
                    0 < basin_map_to_eval[row_index - 1][column_index] < basin_map_to_eval[row_index][column_index]:
                basin_map_to_eval[row_index][column_index] = basin_map_to_eval[row_index - 1][column_index]
            if column_index > 0 and 0 \
                    < basin_map_to_eval[row_index][column_index - 1] < basin_map_to_eval[row_index][column_index]:
                basin_map_to_eval[row_index][column_index] = basin_map_to_eval[row_index][column_index - 1]
            if column_index < len(basin_map_to_eval[row_index]) - 1 and \
                    0 < basin_map_to_eval[row_index][column_index + 1] < basin_map_to_eval[row_index][column_index]:
                basin_map_to_eval[row_index][column_index] = basin_map_to_eval[row_index][column_index + 1]
            if row_index < len(basin_map_to_eval) - 1 and \
                    0 < basin_map_to_eval[row_index + 1][column_index] < basin_map_to_eval[row_index][column_index]:
                basin_map_to_eval[row_index][column_index] = basin_map_to_eval[row_index + 1][column_index]


lines = FileReader('input.txt').get_lines()
data = get_data(lines)
basin_iterator = 1
basin_map = create_basin_map(len(data), len(data[0]))
for row in range(0, len(data)):
    for column in range(0, len(data[row])):
        point = data[row][column]
        if point < 9:
            basin_map[row][column] = get_basin_iterator(basin_map, row, column, basin_iterator)
        elif column > 0 and data[row][column - 1] < 9:
            basin_iterator += 1

for i in range(0, basin_iterator):
    update_basin_map(basin_map)

basin_counts = dict()
for row in range(0, len(data)):
    for column in range(0, len(data[row])):
        if basin_map[row][column] > 0:
            if basin_map[row][column] in basin_counts:
                basin_counts[basin_map[row][column]] += 1
            else:
                basin_counts[basin_map[row][column]] = 1

top_basins = list(map(lambda x: x[1], sorted(basin_counts.items(), key=lambda kv: -kv[1])))[0:3]
result = reduce(lambda x, y: x * y, top_basins)

print('Part 2 Answer: {result}'.format(result=result))
