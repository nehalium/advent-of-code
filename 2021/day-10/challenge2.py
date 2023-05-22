from collections import deque

from utils.filereader import FileReader

print('Hello, Day {day}!'.format(day=10))

char_closers = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}
char_scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

lines = FileReader('input.txt').get_lines()
is_corrupted = False
scores = list()
total_score = 0
for line in lines:
    stack = deque()
    score = 0
    is_corrupted = False
    for char in list(line.strip()):
        if char in char_closers.keys():
            stack.append(char)
        else:
            if len(stack) > 0 and char_closers[stack[-1]] == char:
                stack.pop()
            else:
                is_corrupted = True
    if not is_corrupted:
        for i in range(0, len(stack)):
            score = (score * 5) + char_scores[char_closers[stack.pop()]]
        scores.append(score)

total_score = sorted(scores)[int(len(scores) / 2)]

print('Part 2 Answer: {result}'.format(result=total_score))
