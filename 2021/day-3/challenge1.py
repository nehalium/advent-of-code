from utils.filereader import FileReader

print('Hello, Day {day}!'.format(day=3))

lines = FileReader('input.txt').get_lines()

zero_array = [0] * len(lines[0])
one_array = [0] * len(lines[0])
gamma_bits = ''
gamma_rate = 0
epsilon_bits = ''
epsilon_rate = 0

for line in lines:
    bits = list(line)
    for index in range(0, len(bits)):
        if bits[index] == '0':
            zero_array[index] += 1
        if bits[index] == '1':
            one_array[index] += 1

for index in range(0, len(zero_array)):
    if zero_array[index] > one_array[index]:
        gamma_bits += '0'
        epsilon_bits += '1'
    else:
        gamma_bits += '1'
        epsilon_bits += '0'

gamma_rate = int(gamma_bits, 2)
epsilon_rate = int(epsilon_bits, 2)

print('Part 1 Answer: {result}'.format(result=(gamma_rate * epsilon_rate)))
