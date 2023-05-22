from utils.filereader import FileReader

print('Hello, Day {day}!'.format(day=4))


def read_numbers(lines_to_read):
    return list(map(lambda x: int(x), lines_to_read[0].split(',')))


def read_boards(lines_to_read):
    line_number = 1
    boards_created = list()
    board = list()
    for line in lines_to_read:
        if line_number == 1:
            pass
        elif len(line.strip()) == 0:
            if len(board) > 0:
                boards_created.append(board)
            board = list()
        else:
            board.append(list(map(lambda x: int(x), line.strip().split())))
        line_number += 1
    boards_created.append(board)
    return boards_created


def create_mark_board(number_of_boards, number_of_rows, number_of_columns):
    return [[[0] * number_of_columns for i in range(number_of_rows)] for j in range(number_of_boards)]


def board_wins(board_to_check, row_i, column_i):
    row_to_check = board_to_check[row_i]
    column_to_check = list(map(lambda x: x[column_i], board_to_check))
    if len(list(filter(lambda x: x == 0, row_to_check))) == 0:
        return True
    elif len(list(filter(lambda x: x == 0, column_to_check))) == 0:
        return True
    else:
        return False


def call_numbers(numbers_to_call, boards_to_check, boards_to_mark):
    winning_indexes = list()
    winning_boards = list()
    for number_called in numbers_to_call:
        board_index = 0
        for board_to_check in boards_to_check:
            row_index = 0
            for row in board_to_check:
                column_index = 0
                for column in row:
                    if column == number_called:
                        # make a mark for each matching number
                        boards_to_mark[board_index][row_index][column_index] = 1
                        if board_wins(boards_to_mark[board_index], row_index, column_index):
                            print('Board {board_index} wins.'.format(board_index=board_index))
                            if not winning_indexes.__contains__(board_index):
                                winning_boards.append({
                                    'board_index': board_index,
                                    'row_index': row_index,
                                    'column_index': column_index,
                                    'number': number_called
                                })
                                winning_indexes.append(board_index)
                                if len(winning_indexes) == len(boards_to_mark):
                                    return winning_boards.pop()
                    column_index += 1
                row_index += 1
            board_index += 1
    return winning_boards.pop()


def calculate_score(boards_to_calculate, marked_boards, info):
    unmarked_sum = 0
    row_index = 0
    for row in boards_to_calculate[info['board_index']]:
        column_index = 0
        for column in row:
            if marked_boards[info['board_index']][row_index][column_index] == 0:
                unmarked_sum += column
            column_index += 1
        row_index += 1
    return unmarked_sum * info['number']


lines = FileReader('input.txt').get_lines()
numbers = read_numbers(lines)
boards = read_boards(lines)
mark_boards = create_mark_board(len(boards), len(boards[0]), len(boards[0]))
winning_info = call_numbers(numbers, boards, mark_boards)
winning_score = calculate_score(boards, mark_boards, winning_info)

print('Part 2 Answer: {result}'.format(result=winning_score))
