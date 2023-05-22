import re


class Monkey:

    index = 0
    starting_items = []
    operator = ""
    operand = ""
    test_operand = 0
    true_case = 0
    false_case = 0
    inspected_count = 0

    def __init__(self, first_line):
        self.extract_first_line(first_line)

    def __str__(self):
        return f"Monkey {self.index}: {self.starting_items}"

    @staticmethod
    def is_new_monkey(line):
        return line.startswith("Monkey")

    @staticmethod
    def extract_from_line(regex, line):
        return re.search(regex, line)

    def extract(self, line_index, line):
        if line_index == 1:
            self.extract_first_line(line)
        elif line_index == 2:
            self.extract_second_line(line)
        elif line_index == 3:
            self.extract_third_line(line)
        elif line_index == 4:
            self.extract_fourth_line(line)
        elif line_index == 5:
            self.extract_fifth_line(line)
        elif line_index == 6:
            self.extract_sixth_line(line)

    def extract_first_line(self, first_line):
        self.index = int(self.extract_from_line(r'Monkey\s([0-9]+)', first_line).group(1))

    def extract_second_line(self, second_line):
        items = self.extract_from_line(r'Starting items:\s([0-9|,\s]+)', second_line).group(1)
        self.starting_items = list(map((lambda x: int(x)), items.replace(" ", "").split(",")))

    def extract_third_line(self, third_line):
        matches = self.extract_from_line(r'Operation:\snew\s=\sold\s(.)\s(.+)', third_line)
        if matches.group(2) == "old":
            self.operator = "^"
            self.operand = 2
        else:
            self.operator = matches.group(1)
            self.operand = int(matches.group(2))

    def extract_fourth_line(self, fourth_line):
        self.test_operand = int(self.extract_from_line(r'Test:\sdivisible\sby\s([0-9]+)', fourth_line).group(1))

    def extract_fifth_line(self, fifth_line):
        self.true_case = int(self.extract_from_line(r'If\strue:\sthrow\sto\smonkey\s([0-9]+)', fifth_line).group(1))

    def extract_sixth_line(self, sixth_line):
        self.false_case = int(self.extract_from_line(r'If\sfalse:\sthrow\sto\smonkey\s([0-9]+)', sixth_line).group(1))

    def inspect_items(self, monkeys, magic_number=-1):
        while len(self.starting_items) > 0:
            worry_level = self.starting_items.pop(0)
            worry_level = self.excited_worry_level(worry_level)
            worry_level = self.bored_worry_level(worry_level, magic_number)
            next_monkey_index = self.get_next_monkey_index(worry_level)
            monkeys[next_monkey_index].add_item(worry_level)
            self.inspected_count += 1

    def excited_worry_level(self, worry_level):
        if self.operator == "*":
            return worry_level * self.operand
        elif self.operator == "+":
            return worry_level + self.operand
        elif self.operator == "^":
            return worry_level ** self.operand

    def bored_worry_level(self, worry_level, magic_number):
        if magic_number > -1:
            return worry_level % magic_number
        else:
            return int(worry_level / 3)

    def test_worry_level(self, worry_level):
        return worry_level % self.test_operand == 0

    def get_next_monkey_index(self, worry_level):
        if self.test_worry_level(worry_level):
            return self.true_case
        else:
            return self.false_case

    def add_item(self, item):
        self.starting_items += [item]
