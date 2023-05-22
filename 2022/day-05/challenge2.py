from utils.filereader import FileReader


def move(instruction, s):
    popped = []
    for i in range(1, instruction[0] + 1):
        popped.append(s[instruction[1]].pop())
    while len(popped) > 0:
        s[instruction[2]].append(popped.pop())


print('Hello, Day {day}!'.format(day=5))

lines = FileReader('input.txt').get_lines()

mode = 0
stacks = {}
crates = []
stack_count = 0
instructions = []

for line in lines:
    if '[' in line:
        mode = 1  # stack information mode
    elif line.startswith("move"):
        mode = 3  # instructions mode
    elif line == "\n":
        mode = 0  # blank row
    else:
        mode = 2  # stack indices mode

    if mode == 0:  # do nothing
        pass
    elif mode == 1:  # read stack information
        crates.append([line[i:i+1] for i in range(1, len(line), 4)])
    elif mode == 2:  # read stack indices
        stack_count = len([i for i in range(1, len(line), 4)])
    else:  # read instructions
        line_parts = line.split(' ')
        instructions.append([int(line_parts[1]), int(line_parts[3]), int(line_parts[5])])

# pad crate lists
crates = list(map((lambda x: x + [''] * (stack_count - len(x))), crates))

# transpose crate lists to stacks dictionary
stacks = dict(zip(range(1, stack_count + 1), list(map(list, zip(*crates)))))

# reverse the lists to make the bottommost item the first item in the array
for i in stacks:
    stacks[i].reverse()
    stacks[i] = list(filter((lambda x: x.strip(' ') != ''), stacks[i]))

# execute instructions
for i in instructions:
    move(i, stacks)

tops = list(map((lambda x: x[1].pop()), stacks.items()))

print('Part 2 Answer: {result}'.format(result="".join(tops)))
