from utils.filereader import FileReader
from elevation_step import ElevationStep


def build_tree(s, hmap, current_node, completed):
    current_el = hmap[s[0]][s[1]]
    if current_el == "S":
        current_el = "a"
    if current_el == "E":
        completed.append(current_node)
        return
    target_el = chr(ord(current_el) + 1)  # get the next elevation
    next_path = (s[0] - 1, s[1])  # look up
    if s[0] > 0:
        next_el = hmap[next_path[0]][next_path[1]]
        if next_el == "E":
            next_el = "z"
        if ord(next_el) <= ord(target_el):
            next_node = ElevationStep(next_path)
            current_node.add_child(next_node)
            if not current_node.contains(next_path):
                build_tree(next_path, hmap, next_node, completed)
    next_path = (s[0] + 1, s[1])  # look down
    if s[0] < len(hmap) - 1:
        next_el = hmap[next_path[0]][next_path[1]]
        if next_el == "E":
            next_el = "z"
        if ord(next_el) <= ord(target_el):
            next_node = ElevationStep(next_path)
            current_node.add_child(next_node)
            if not current_node.contains(next_path):
                build_tree(next_path, hmap, next_node, completed)
    next_path = (s[0], s[1] - 1)  # look left
    if s[1] > 0:
        next_el = hmap[next_path[0]][next_path[1]]
        if next_el == "E":
            next_el = "z"
        if ord(next_el) <= ord(target_el):
            next_node = ElevationStep(next_path)
            current_node.add_child(next_node)
            if not current_node.contains(next_path):
                build_tree(next_path, hmap, next_node, completed)
    next_path = (s[0], s[1] + 1)  # look right
    if s[1] < len(hmap[0]) - 1:
        next_el = hmap[next_path[0]][next_path[1]]
        if next_el == "E":
            next_el = "z"
        if ord(next_el) <= ord(target_el):
            next_node = ElevationStep(next_path)
            current_node.add_child(next_node)
            if not current_node.contains(next_path):
                build_tree(next_path, hmap, next_node, completed)
    return


def build_tree_reverse(s, hmap, current_node, completed):
    current_el = hmap[s[0]][s[1]]
    if current_el == "E":
        current_el = "z"
    if current_el == "S":
        completed.append(current_node)
        return
    target_el = chr(ord(current_el) - 1)  # get the next elevation
    next_path = (s[0] - 1, s[1])  # look up
    if s[0] > 0:
        next_el = hmap[next_path[0]][next_path[1]]
        if next_el == "S":
            next_el = "a"
        if ord(next_el) >= ord(target_el):
            next_node = ElevationStep(next_path)
            current_node.add_child(next_node)
            if not current_node.contains(next_path):
                build_tree_reverse(next_path, hmap, next_node, completed)
    next_path = (s[0] + 1, s[1])  # look down
    if s[0] < len(hmap) - 1:
        next_el = hmap[next_path[0]][next_path[1]]
        if next_el == "S":
            next_el = "a"
        if ord(next_el) >= ord(target_el):
            next_node = ElevationStep(next_path)
            current_node.add_child(next_node)
            if not current_node.contains(next_path):
                build_tree_reverse(next_path, hmap, next_node, completed)
    next_path = (s[0], s[1] - 1)  # look left
    if s[1] > 0:
        next_el = hmap[next_path[0]][next_path[1]]
        if next_el == "S":
            next_el = "a"
        if ord(next_el) >= ord(target_el):
            next_node = ElevationStep(next_path)
            current_node.add_child(next_node)
            if not current_node.contains(next_path):
                build_tree_reverse(next_path, hmap, next_node, completed)
    next_path = (s[0], s[1] + 1)  # look right
    if s[1] < len(hmap[0]) - 1:
        next_el = hmap[next_path[0]][next_path[1]]
        if next_el == "S":
            next_el = "a"
        if ord(next_el) >= ord(target_el):
            next_node = ElevationStep(next_path)
            current_node.add_child(next_node)
            if not current_node.contains(next_path):
                build_tree_reverse(next_path, hmap, next_node, completed)
    return


print('Hello, Day {day}!'.format(day=12))

lines = FileReader('input.txt').get_lines()

heatmap = []
line_number = 0
starting_position = (0, 0)
ending_position = (0, 0)
completed_leaves = []

for line in lines:
    heatmap.append(line.strip("\n"))
    if line.find("S") > -1:
        starting_position = line_number, line.find("S")
    if line.find("E") > -1:
        ending_position = line_number, line.find("E")
    line_number += 1

starting_node = ElevationStep(starting_position)
build_tree(starting_position, heatmap, starting_node, completed_leaves)

#ending_node = ElevationStep(ending_position)
#build_tree_reverse(ending_position, heatmap, ending_node, completed_leaves)

completed_paths = list(map((lambda x: x.path), completed_leaves))

completed_lengths = list(map((lambda x: len(x.path) - 1), completed_leaves))
completed_lengths.sort()
total = completed_lengths[1]

print('Part 1 Answer: {result}'.format(result=total))
