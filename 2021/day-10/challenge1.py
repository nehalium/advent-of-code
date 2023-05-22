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
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

lines = FileReader('input.txt').get_lines()
score = 0
for line in lines:
    stack = deque()
    first_illegal_char = ''
    for char in list(line.strip()):
        if char in char_closers.keys():
            stack.append(char)
        else:
            if len(stack) > 0 and char_closers[stack[-1]] == char:
                stack.pop()
            else:
                score += char_scores[char]
                break

print('Part 1 Answer: {result}'.format(result=score))
