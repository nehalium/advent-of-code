from utils.filereader import FileReader


def print_screen(pixels, width):
    for i in range(int(len(pixels) / width)):
        print("".join(pixels[(i * width):(i * width) + width]))


def update_pixel(new_position, width):
    return "###".rjust(new_position + 2, ".").ljust(width, ".")


print('Hello, Day {day}!'.format(day=10))

lines = FileReader('input.txt').get_lines()

x = 1
ops = [0]
cycle_num = 1
screen_width = 40
pixel = "###".ljust(screen_width, ".")
crt = []
total = 0

for line in lines:
    parts = line.strip("\n").split(" ")
    if parts[0] == "noop":
        ops += [0]
    elif parts[0] == "addx":
        ops += [0]
        ops += [int(parts[1])]

while len(ops) > 0:
    x += ops.pop(0)
    pixel = update_pixel(x, screen_width)
    crt += pixel[(cycle_num % screen_width) - 1]
    cycle_num += 1


print('Part 2 Answer:')
print_screen(crt, screen_width)