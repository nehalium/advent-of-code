import math

from utils.filereader import FileReader


def move_head(d, h):
    h += [next_location(h[len(h) - 1], get_move_vector(d))]


def get_move_vector(d):
    if d == "U":
        return 0, 1
    elif d == "D":
        return 0, -1
    elif d == "L":
        return -1, 0
    elif d == "R":
        return 1, 0


def next_location(knot, move_vector):
    return tuple(map(lambda i, j: i + j, knot, move_vector))


def update_tail(h, t):
    last_h = h[len(h) - 1]
    last_t = t[len(t) - 1]
    if has_no_slack(last_h, last_t):
        t += [move_tail(last_h, last_t)]


def has_no_slack(last_h, last_t):
    return calculate_distance(last_h, last_t) >= 2


def calculate_distance(point1, point2):
    return math.sqrt(((point1[0] - point2[0]) ** 2) + ((point1[1] - point2[1]) ** 2))


def move_tail(last_h, last_t):
    if last_h[0] == last_t[0]:
        if last_h[1] > last_t[1]:
            return next_location(last_t, (0, 1))
        else:
            return next_location(last_t, (0, -1))
    elif last_h[1] == last_t[1]:
        if last_h[0] > last_t[0]:
            return next_location(last_t, (1, 0))
        else:
            return next_location(last_t, (-1, 0))
    else:
        if last_h[0] > last_t[0] and last_h[1] > last_t[1]:
            return next_location(last_t, (1, 1))
        elif last_h[0] > last_t[0] and last_h[1] < last_t[1]:
            return next_location(last_t, (1, -1))
        elif last_h[0] < last_t[0] and last_h[1] > last_t[1]:
            return next_location(last_t, (-1, 1))
        elif last_h[0] < last_t[0] and last_h[1] < last_t[1]:
            return next_location(last_t, (-1, -1))


def move(d, s, h, t_dict):
    for i in range(s):
        move_head(d, h)
        update_tail(h, t_dict[1])
        for j in range(1, 9):
            update_tail(t_dict[j], t_dict[j + 1])


print('Hello, Day {day}!'.format(day=9))

lines = FileReader('input.txt').get_lines()

head_hops = [(0, 0)]
tail_dict = {}
total = 0

# initialize tail dictionary
for tail_element in range(1, 10):
    tail_dict[tail_element] = [(0, 0)]

for line in lines:
    direction, steps = line.split(" ")
    move(direction, int(steps), head_hops, tail_dict)

total = len(list(dict.fromkeys(tail_dict[9])))  # dedupe and count

print('Part 2 Answer: {result}'.format(result=total))
