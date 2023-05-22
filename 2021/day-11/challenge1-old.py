from utils.filereader import FileReader

print('Hello, Day {day}!'.format(day=11))


def get_data(lines_to_process):
    data_list = list()
    for line in lines_to_process:
        data_list.append(list(map(lambda x: int(x), list(line.strip()))))
    return data_list


def print_data(data_to_print, step):
    print('--STEP {step}--'.format(step=step))
    print(str(data_to_print).replace('],', '\n').replace('[', '').replace(']', '').replace(',', '').replace(' ', ''))


def visit_neighbors(data_to_eval, row_index, column_index, f):
    f = update_octopus(data_to_eval, row_index - 1, column_index - 1, f)
    f = update_octopus(data_to_eval, row_index - 1, column_index, f)
    f = update_octopus(data_to_eval, row_index - 1, column_index + 1, f)
    f = update_octopus(data_to_eval, row_index, column_index - 1, f)
    f = update_octopus(data_to_eval, row_index, column_index + 1, f)
    f = update_octopus(data_to_eval, row_index + 1, column_index - 1, f)
    f = update_octopus(data_to_eval, row_index + 1, column_index, f)
    f = update_octopus(data_to_eval, row_index + 1, column_index + 1, f)
    return f


def update_octopus(data_to_eval, row_index, column_index, f):
    if row_index < 0:
        return f
    if column_index < 0:
        return f
    if row_index >= len(data_to_eval):
        return f
    if column_index >= len(data_to_eval[0]):
        return f
    if data_to_eval[row_index][column_index] < 9:
        data_to_eval[row_index][column_index] += 1
        return f
    else:
        data_to_eval[row_index][column_index] = 0
        f += 1
        return visit_neighbors(data_to_eval, row_index, column_index, f)


lines = FileReader('test1.txt').get_lines()
data = get_data(lines)
steps = 2
flashes = 0
print_data(data, 0)
for step in range(1, steps + 1):
    for row in range(0, len(data)):
        for column in range(0, len(data[row])):
            flashes = update_octopus(data, row, column, flashes)
    print_data(data, step)

print('Part 1 Answer: {result}'.format(result=flashes))
