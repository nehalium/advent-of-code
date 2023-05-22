from utils.filereader import FileReader

print('Hello, Day {day}!'.format(day=9))


def get_data(lines_to_process):
    data_list = list()
    for line in lines_to_process:
        data_list.append(list(map(lambda x: int(x), list(line.strip()))))
    return data_list


def is_low_point(row_index, column_index, data_to_eval):
    point = data_to_eval[row_index][column_index]
    if row_index > 0 and point >= data_to_eval[row_index - 1][column_index]:
        return False
    if column_index > 0 and point >= data_to_eval[row_index][column_index - 1]:
        return False
    if column_index < len(data_to_eval[row_index]) - 1 and point >= data_to_eval[row_index][column_index + 1]:
        return False
    if row_index < len(data_to_eval) - 1 and point >= data_to_eval[row_index + 1][column_index]:
        return False
    return True


lines = FileReader('input.txt').get_lines()
data = get_data(lines)
low_points = list()
for row in range(0, len(data)):
    for column in range(0, len(data[row])):
        if is_low_point(row, column, data):
            low_points.append(data[row][column])
risk_level = sum(list(map(lambda x: x + 1, low_points)))

print('Part 1 Answer: {result}'.format(result=risk_level))
