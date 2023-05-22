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


def update_all_neighbors(data_to_eval, row_index, column_index):
    update_neighbor(data_to_eval, row_index - 1, column_index - 1)
    update_neighbor(data_to_eval, row_index - 1, column_index)
    update_neighbor(data_to_eval, row_index - 1, column_index + 1)
    update_neighbor(data_to_eval, row_index, column_index - 1)
    update_neighbor(data_to_eval, row_index, column_index + 1)
    update_neighbor(data_to_eval, row_index + 1, column_index - 1)
    update_neighbor(data_to_eval, row_index + 1, column_index)
    update_neighbor(data_to_eval, row_index + 1, column_index + 1)


def update_neighbor(data_to_eval, row_index, column_index):
    if row_index < 0:
        return
    if column_index < 0:
        return
    if row_index >= len(data_to_eval):
        return
    if column_index >= len(data_to_eval[0]):
        return
    data_to_eval[row_index][column_index] += 1


def reset_all_octopuses(data_to_eval):
    for row in range(0, len(data_to_eval)):
        for column in range(0, len(data_to_eval[row])):
            if data_to_eval[row][column] > 9:
                data_to_eval[row][column] = 0


def flash_all_octopuses(data_to_eval):
    for row in range(0, len(data_to_eval)):
        for column in range(0, len(data_to_eval[row])):
            if data_to_eval[row][column] > 9:
                update_all_neighbors(data_to_eval, row, column)


def update_all_octopuses(data_to_eval):
    for row in range(0, len(data_to_eval)):
        for column in range(0, len(data_to_eval[row])):
            data_to_eval[row][column] += 1


lines = FileReader('test.txt').get_lines()
data = get_data(lines)
steps = 2
flashes = 0
print_data(data, 0)
for step in range(1, steps + 1):
    update_all_octopuses(data)
    flash_all_octopuses(data)
    reset_all_octopuses(data)
    print_data(data, step)

print('Part 1 Answer: {result}'.format(result=flashes))