from functools import reduce

from utils.harness import Harness


# EXAMPLE:
# 30373 => 00000
# 25512    01410
# 65332    02240
# 33549    02820
# 35390    00000
def get_views(row, col, tree_map):
    if row == 0 or col == 0 or row == len(tree_map) - 1 or col == len(tree_map[0]) - 1:
        return 0
    # preceding rows
    up = 0
    for r in range(row - 1, -1, -1):
        up += 1
        if tree_map[r][col] >= tree_map[row][col]:
            break
    # preceding columns
    left = 0
    for c in range(col - 1, -1, -1):
        left += 1
        if tree_map[row][c] >= tree_map[row][col]:
            break
    # proceeding rows
    down = 0
    for r in range(row + 1, len(tree_map)):
        down += 1
        if tree_map[r][col] >= tree_map[row][col]:
            break
    # proceeding columns
    right = 0
    for c in range(col + 1, len(tree_map[0])):
        right += 1
        if tree_map[row][c] >= tree_map[row][col]:
            break
    return up * left * down * right


def print_tree_map(t):
    for i in range(len(t)):
        print(str(t[i]))


def print_view_map(v):
    for i in range(len(v)):
        print(str(v[i]).replace("True", "T").replace("False", "F"))


harness = Harness(day=8, part_num=2, filename='input.txt')
harness.write_header()
lines = harness.read_file()

trees = []
views = []
sorted_views = []
total = 0

for line in lines:
    tree_row = list(map((lambda x: int(x)), line.strip("\n")))
    trees.append(tree_row)
    views.append([0] * len(tree_row))

for i in range(len(trees)):
    for j in range(len(trees[0])):
        views[i][j] = get_views(i, j, trees)

sorted_views = reduce((lambda x, y: x + y), views)
sorted_views.sort()
sorted_views.reverse()

harness.write_result(sorted_views[0])