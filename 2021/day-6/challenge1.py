from utils.filereader import FileReader

print('Hello, Day {day}!'.format(day=6))

data = FileReader('input.txt').get_lines()
fish_list = list(map(lambda x: int(x), data[0].split(',')))
days = 80
for day in range(1, days + 1):
    for fish_index in range(0, len(fish_list)):
        if fish_list[fish_index] == 0:
            fish_list[fish_index] = 6
            fish_list.append(8)
        else:
            fish_list[fish_index] -= 1

print('Part 1 Answer: {result}'.format(result=len(fish_list)))
