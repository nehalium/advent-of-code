import sys

from utils.filereader import FileReader


class Interface:

    @staticmethod
    def write_header(day):
        print('Hello, Day {day}!'.format(day=day))

    @staticmethod
    def write_result(part_num, result):
        print('Part {part_num} Answer: {result}'.format(part_num=part_num, result=result))

    @staticmethod
    def read_file(filename):
        return FileReader(filename).get_lines()
