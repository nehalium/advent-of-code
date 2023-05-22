from utils.filereader import FileReader


class Harness:

    day = 1
    part_num = 1
    filename = "test.txt"

    def __init__(self, day, part_num, filename):
        self.day = day
        self.part_num = part_num
        self.filename = filename

    def write_header(self):
        print('Hello, Day {day}!'.format(day=self.day))

    def write_result(self, result):
        print('Part {part_num} Answer: {result}'.format(part_num=self.part_num, result=result))

    def read_file(self):
        return FileReader(self.filename).get_lines()
