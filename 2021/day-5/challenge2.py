from utils.filereader import FileReader

print('Hello, Day {day}!'.format(day=5))


def parse_input(input_lines):
    tuples_to_build = list()
    for line in input_lines:
        tuples_to_build.append(parse_line(line))
    return tuples_to_build


def parse_line(line_to_parse):
    line_parts = line_to_parse.split('->')
    first_tuple = tuple(map(lambda x: int(x), line_parts[0].strip().split(',')))
    second_tuple = tuple(map(lambda x: int(x), line_parts[1].strip().split(',')))
    return first_tuple, second_tuple


def is_horizontal(tuple_to_evaluate):
    return tuple_to_evaluate[0][1] == tuple_to_evaluate[1][1]


def is_vertical(tuple_to_evaluate):
    return tuple_to_evaluate[0][0] == tuple_to_evaluate[1][0]


def calculate_slope(coordinates):
    if coordinates[1][0] == coordinates[0][0]:
        return 9999.0
    return (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])


def smallest_x(coordinates):
    if coordinates[0][0] < coordinates[1][0]:
        return coordinates[0]
    else:
        return coordinates[1]


def calculate_new_y(slope, coordinates, new_x):
    coordinate = smallest_x(coordinates)
    return (int(slope) * (new_x - coordinate[0])) + coordinate[1]


def expand_tuples(tuples_to_evaluate):
    tuples_list = list()
    for t in tuples_to_evaluate:
        if is_horizontal(t):
            for i in range(min(t[0][0], t[1][0]), max(t[0][0], t[1][0]) + 1):
                tuples_list.append((i, t[0][1]))
        elif is_vertical(t):
            for i in range(min(t[0][1], t[1][1]), max(t[0][1], t[1][1]) + 1):
                tuples_list.append((t[0][0], i))
        else:
            slope = calculate_slope(t)
            if abs(slope) == 1.0:
                for i in range(min(t[0][0], t[1][0]), max(t[0][0], t[1][0]) + 1):
                    tuples_list.append((i, calculate_new_y(slope, t, i)))
    return tuples_list


def get_counts(tuples_to_evaluate):
    tuple_dict = dict()
    for t in tuples_to_evaluate:
        if t in tuple_dict:
            tuple_dict[t] += 1
        else:
            tuple_dict[t] = 1
    return tuple_dict


def filter_counts(counts):
    return dict(filter(lambda x: x[1] >= 2, counts.items()))


lines = FileReader('input.txt').get_lines()
tuples = parse_input(lines)
expanded_tuples = expand_tuples(tuples)
tuple_counts = get_counts(expanded_tuples)
filtered_counts = filter_counts(tuple_counts)

print('Part 2 Answer: {result}'.format(result=len(filtered_counts)))
