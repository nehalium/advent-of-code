from utils.filereader import FileReader

print('Hello, Day {day}!'.format(day=3))

lines = FileReader('input.txt').get_lines()

zero_array = [0] * len(lines[0])
one_array = [0] * len(lines[0])
oxygen_generator_rating = 0
co2_scrubber_rating = 0


def oxygen_filter(val, i):
    if zero_array[i] > one_array[i]:
        return list(val)[i] == '0'
    elif zero_array[i] < one_array[i]:
        return list(val)[i] == '1'
    else:
        return list(val)[i] == '1'


iteration = 0
oxygen_values = lines
while len(oxygen_values) != 1:
    zero_array = [0] * len(lines[0])
    one_array = [0] * len(lines[0])
    for oxygen_value in oxygen_values:
        bits = list(oxygen_value)
        for index in range(0, len(bits)):
            if bits[index] == '0':
                zero_array[index] += 1
            if bits[index] == '1':
                one_array[index] += 1
    oxygen_values = list(filter(lambda x: oxygen_filter(x, iteration), oxygen_values))
    iteration += 1


def co2_filter(val, i):
    if zero_array[i] < one_array[i]:
        return list(val)[i] == '0'
    elif zero_array[i] > one_array[i]:
        return list(val)[i] == '1'
    else:
        return list(val)[i] == '0'


iteration = 0
co2_values = lines
while len(co2_values) != 1:
    zero_array = [0] * len(lines[0])
    one_array = [0] * len(lines[0])
    for co2_value in co2_values:
        bits = list(co2_value)
        for index in range(0, len(bits)):
            if bits[index] == '0':
                zero_array[index] += 1
            if bits[index] == '1':
                one_array[index] += 1
    co2_values = list(filter(lambda x: co2_filter(x, iteration), co2_values))
    iteration += 1

oxygen_generator_rating = int(oxygen_values[0], 2)
co2_scrubber_rating = int(co2_values[0], 2)

print('Part 2 Answer: {result}'.format(result=(oxygen_generator_rating * co2_scrubber_rating)))
