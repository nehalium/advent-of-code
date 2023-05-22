import statistics

from utils.filereader import FileReader

print('Hello, Day {day}!'.format(day=5))


def calculate_fuel_spent(steps):
    return steps * (steps + 1) / 2


def calculate_total_fuel_spent(positions_to_eval, target):
    return int(sum(list(map(lambda x: calculate_fuel_spent(abs(x - target)), positions_to_eval))))


data = FileReader('input.txt').get_lines()
positions = list(map(lambda x: int(x), data[0].split(',')))
fuel_spent_list = list(map(lambda x: calculate_total_fuel_spent(positions, x), range(min(positions), max(positions) + 1)))

print('Part 2 Answer: {result}'.format(result=min(fuel_spent_list)))
