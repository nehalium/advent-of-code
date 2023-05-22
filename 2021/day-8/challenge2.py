from utils.filereader import FileReader

print('Hello, Day {day}!'.format(day=8))

display_segments = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg'
}
displays_by_count = {
    2: [1],
    3: [7],
    4: [4],
    5: [2, 3, 5],
    6: [0, 6, 9],
    7: [8]
}


def initialize_display_mapping():
    return {
        'a': '',
        'b': '',
        'c': '',
        'd': '',
        'e': '',
        'f': '',
        'g': ''
    }


def initialize_possible_values():
    return {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: []
    }


def get_possible_values(signal_patterns_to_eval):
    possible_values_list = initialize_possible_values()
    for pattern in signal_patterns_to_eval:
        for display in displays_by_count[len(pattern)]:
            possible_values_list[display].append(pattern)
    return possible_values_list


def diff_segments(check_this, against_this):
    return list(filter(lambda x: x not in against_this, check_this))


def get_missing_segment(check_this, against_this):
    return diff_segments(check_this, against_this)[0]


def overlaps(check_this, against_this):
    return all([c in against_this for c in check_this])


def matches(check_this, against_this):
    return sorted(check_this) == sorted(against_this)


def get_3(possible_values_to_eval):
    possible_235 = [
        diff_segments(possible_values_to_eval[2][0], possible_values_to_eval[2][1]),
        diff_segments(possible_values_to_eval[2][1], possible_values_to_eval[2][2]),
        diff_segments(possible_values_to_eval[2][0], possible_values_to_eval[2][2])
    ]
    possible_235_len = list(map(lambda x: len(x), possible_235))
    if possible_235_len == [1, 1, 2]:
        return possible_values_to_eval[2][1]
    if possible_235_len == [1, 2, 1]:
        return possible_values_to_eval[2][0]
    if possible_235_len == [2, 1, 1]:
        return possible_values_to_eval[2][2]


def get_6(possible_values_to_eval):
    for segment in possible_values_to_eval[0]:
        if not overlaps(possible_values_to_eval[1], segment):
            return segment


def get_9(possible_values_to_eval):
    if overlaps(possible_values_to_eval[3], possible_values_to_eval[9][0]):
        return possible_values_to_eval[9][0]
    else:
        return possible_values_to_eval[9][1]


def get_5(possible_values_to_eval):
    if overlaps(possible_values_to_eval[5][0], possible_values_to_eval[6]):
        return possible_values_to_eval[5][0]
    else:
        return possible_values_to_eval[5][1]


def get_output_value(output_pattern_to_check, possible_values_to_eval):
    for k, v in possible_values_to_eval.items():
        if matches(v, output_pattern_to_check):
            return k


lines = FileReader('input.txt').get_lines()
sum_of_numeric_values = 0
for line in lines:
    line_parts = line.split('|')
    signal_patterns = line_parts[0].strip().split()
    output_patterns = line_parts[1].strip().split()

    possible_values = get_possible_values(signal_patterns)
    possible_values[1] = possible_values[1][0]
    possible_values[4] = possible_values[4][0]
    possible_values[7] = possible_values[7][0]
    possible_values[8] = possible_values[8][0]
    possible_values[3] = get_3(possible_values)
    possible_values[2].remove(possible_values[3])
    possible_values[5].remove(possible_values[3])
    possible_values[6] = get_6(possible_values)
    possible_values[0].remove(possible_values[6])
    possible_values[9].remove(possible_values[6])
    possible_values[9] = get_9(possible_values)
    possible_values[0].remove(possible_values[9])
    possible_values[0] = possible_values[0][0]
    possible_values[5] = get_5(possible_values)
    possible_values[2].remove(possible_values[5])
    possible_values[2] = possible_values[2][0]

    numeric_value = 0
    for output_pattern in output_patterns:
        output_value = get_output_value(output_pattern, possible_values)
        numeric_value = int(str(numeric_value) + str(output_value))
    sum_of_numeric_values += numeric_value

print('Part 2 Answer: {result}'.format(result=sum_of_numeric_values))
