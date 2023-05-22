from utils.filereader import FileReader


def explode_range(r):
    a, b = r.split('-')
    a, b = int(a), int(b)
    return list(range(a, b + 1))


def get_overlaps(pair):
    return list(set(pair[0]) & set(pair[1]))


print('Hello, Day {day}!'.format(day=4))

lines = FileReader('input.txt').get_lines()

pairs = []
pair_counts = []
overlaps = []
overlap_counts = []
total = 0

for line in lines:
    pairs.append(list(map(explode_range, line.strip('\n').split(','))))

pair_counts = list(map((lambda x: [len(x[0]), len(x[1])]), pairs))
overlaps = list(map(get_overlaps, pairs))
overlap_counts = list(map((lambda x: len(x)), overlaps))

total = len([item for item in overlap_counts if item > 0])

print('Part 2 Answer: {result}'.format(result=total))
