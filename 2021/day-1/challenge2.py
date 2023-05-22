from utils.filereader import FileReader

print('Hello, Day {day}!'.format(day=1))

lines = FileReader('input.txt').get_lines()

iteration = 0
count = 0
previous_window = 0
window_size = 3
windows = list()

for line in lines:
    windows.append(int(line))
    for windowIndex in range(len(windows) - 2, len(windows) - (2 + window_size - 1), -1):
        if windowIndex < 0:
            break
        windows[windowIndex] += int(line)
    iteration += 1

for index in range(0, window_size - 1):
    windows.pop()

iteration = 0

for window in windows:
    if iteration > 0:
        if previous_window < int(window):
            count += 1
    previous_window = int(window)
    iteration += 1

print('Part 2 Answer: {result}'.format(result=count))
