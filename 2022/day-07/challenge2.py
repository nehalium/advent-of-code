from functools import reduce
from utils.interface import Interface


def path_str(path):
    return "/".join(path).replace("//", "/")


def recurse_sizes(new_size, d_sizes, d, d_parents):
    if path_str(d) not in d_sizes:
        d_sizes[path_str(d)] = 0
    d_sizes[path_str(d)] += new_size
    if d != "/":
        recurse_sizes(new_size, d_sizes, d_parents[d], d_parents)


Interface.write_header(7)

lines = Interface.read_file('input.txt')

current_path = ["/"]
parents = {"/": "/"}
sizes = {"/": 0}
mode = 0  # 0 = command mode, 1 = ls results mode
eligible = []

for line in lines:
    parts = line.strip("\n").split(" ")
    if parts[0] == "$":  # command mode
        mode = 0  # reset mode
        if parts[1] == "cd":
            if parts[2] == "/":
                current_path = ["/"]
            elif parts[2] == "..":
                current_path.pop()
            else:
                current_path.append(parts[2])
        elif parts[1] == "ls":
            mode = 1
    else:  # results mode
        if mode == 1:  # ls mode
            if parts[0] == "dir":  # new directory
                if parts[1] not in parents:
                    parents[path_str(current_path + [parts[1]])] = path_str(current_path)
            else:  # new file
                recurse_sizes(int(parts[0]), sizes, path_str(current_path), parents)

eligible = [v for k, v in sizes.items() if v >= (30000000 - (70000000 - sizes["/"]))]
eligible.sort()

Interface.write_result(2, eligible[0])
