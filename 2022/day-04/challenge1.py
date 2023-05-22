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
overlaps_contained = []
total = 0

for line in lines:
    pairs.append(list(map(explode_range, line.strip('\n').split(','))))

pair_counts = list(map((lambda x: [len(x[0]), len(x[1])]), pairs))
overlaps = list(map(get_overlaps, pairs))
overlap_counts = list(map((lambda x: len(x)), overlaps))
overlaps_contained = list(map((lambda x, y: x[0] == y or x[1] == y), pair_counts, overlap_counts))

total = len([item for item in overlaps_contained if item])

print('Part 1 Answer: {result}'.format(result=total))
