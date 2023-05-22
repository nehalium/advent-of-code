from utils.filereader import FileReader

print('Hello, Day {day}!'.format(day=6))

data = FileReader('input.txt').get_lines()
fish_list = list(map(lambda x: int(x), data[0].split(',')))
days = 256
fish_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

for fish in fish_list:
    fish_dict[fish] += 1

for day in range(1, days + 1):
    original_zero = fish_dict[0]
    fish_dict[0] = 0
    for fish in fish_dict:
        if fish > 0:
            fish_dict[fish - 1] += fish_dict[fish]
            fish_dict[fish] = 0
    fish_dict[8] += original_zero
    fish_dict[6] += original_zero

print('Part 2 Answer: {result}'.format(result=sum(fish_dict.values())))
