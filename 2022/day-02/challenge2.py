from functools import reduce

from utils.filereader import FileReader


def first_score(play_round):
    if play_round[1] == 'A':
        return 1
    if play_round[1] == 'B':
        return 2
    if play_round[1] == 'C':
        return 3


def second_score(play_round):
    if play_round[0] == 'A' and play_round[1] == 'A':  # rock, rock
        return 3
    if play_round[0] == 'A' and play_round[1] == 'B':  # rock, paper
        return 6
    if play_round[0] == 'A' and play_round[1] == 'C':  # rock, scissors
        return 0
    if play_round[0] == 'B' and play_round[1] == 'A':  # paper, rock
        return 0
    if play_round[0] == 'B' and play_round[1] == 'B':  # paper, paper
        return 3
    if play_round[0] == 'B' and play_round[1] == 'C':  # paper, scissors
        return 6
    if play_round[0] == 'C' and play_round[1] == 'A':  # scissors, rock
        return 6
    if play_round[0] == 'C' and play_round[1] == 'B':  # scissors, paper
        return 0
    if play_round[0] == 'C' and play_round[1] == 'C':  # scissors, scissors
        return 3


def convert_round(play_round):
    if play_round[0] == 'A' and play_round[1] == 'X':  # rock, lose
        return 'C'
    if play_round[0] == 'A' and play_round[1] == 'Y':  # rock, draw
        return 'A'
    if play_round[0] == 'A' and play_round[1] == 'Z':  # rock, win
        return 'B'
    if play_round[0] == 'B' and play_round[1] == 'X':  # paper, lose
        return 'A'
    if play_round[0] == 'B' and play_round[1] == 'Y':  # paper, draw
        return 'B'
    if play_round[0] == 'B' and play_round[1] == 'Z':  # paper, win
        return 'C'
    if play_round[0] == 'C' and play_round[1] == 'X':  # scissors, lose
        return 'B'
    if play_round[0] == 'C' and play_round[1] == 'Y':  # scissors, draw
        return 'C'
    if play_round[0] == 'C' and play_round[1] == 'Z':  # scissors, win
        return 'A'


def calculate_score(play_round):
    play_round = (play_round[0], convert_round(play_round))
    return first_score(play_round) + second_score(play_round)


print('Hello, Day {day}!'.format(day=2))

lines = FileReader('input.txt').get_lines()

scores = []
total = 0

for line in lines:
    scores.append(calculate_score(line.strip('\n').split(' ')))

total = reduce((lambda x, y: x + y), scores)

print('Part 2 Answer: {result}'.format(result=total))
