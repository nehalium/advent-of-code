from functools import reduce

from utils.harness import Harness


# EXAMPLE:
# 30373 => TTTTT
# 25512    TTTFT
# 65332    TTFTT
# 33549    TFTFT
# 35390    TTTTT
def is_visible(row, col, tree_map):
    # edges are always visible
    if row == 0 or col == 0 or row == len(tree_map) - 1 or col == len(tree_map[0]) - 1:
        return True
    # preceding rows
    cover_found = False
    for r in range(row - 1, -1, -1):
        if tree_map[r][col] >= tree_map[row][col]:
            cover_found = True
    if not cover_found:
        return True
    # preceding columns
    cover_found = False
    for c in range(col - 1, -1, -1):
        if tree_map[row][c] >= tree_map[row][col]:
            cover_found = True
    if not cover_found:
        return True
    # proceeding rows
    cover_found = False
    for r in range(row + 1, len(tree_map)):
        if tree_map[r][col] >= tree_map[row][col]:
            cover_found = True
    if not cover_found:
        return True
    # proceeding columns
    cover_found = False
    for c in range(col + 1, len(tree_map[0])):
        if tree_map[row][c] >= tree_map[row][col]:
            cover_found = True
    if not cover_found:
        return True
    return False


def print_tree_map(t):
    for i in range(len(t)):
        print(str(t[i]))


def print_visibilities(v):
    for i in range(len(v)):
        print(str(v[i]).replace("True", "T").replace("False", "F"))


harness = Harness(day=8, part_num=1, filename='input.txt')
harness.write_header()
lines = harness.read_file()

trees = []
visibilities = []
total = 0

for line in lines:
    tree_row = list(map((lambda x: int(x)), line.strip("\n")))
    trees.append(tree_row)
    visibilities.append([True] * len(tree_row))

for i in range(len(trees)):
    for j in range(len(trees[0])):
        visibilities[i][j] = is_visible(i, j, trees)

total = len([v for v in reduce((lambda x, y: x + y), visibilities) if v])

harness.write_result(total)
