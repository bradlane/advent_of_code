import re


def get_initial_stacks(input_str):
    stacks = [[] for i in range(stack_qty)]  # init stacks lists

    for line in input_str:  # i in range((stack_height - 1), -1, -1):
        for j in range(1, len(line), 4):
            crate_num = (j - 1) // 4
            box = line[j]
            if box != " ":
                stacks[crate_num].insert(0, box)
    return stacks


# get input from input.txt file
with open("input.txt") as f:
    puzzle_input = f.readlines()
    puzzle_input = [line for line in puzzle_input]

# split input between stacks layout and instructions
stacks_lines = puzzle_input[0 : puzzle_input.index("\n") - 1]
move_lines = puzzle_input[puzzle_input.index("\n") + 1 : :]

# parse stacks
stack_qty = len(puzzle_input[0]) // 4
stacks = get_initial_stacks(stacks_lines)

pattern = re.compile(r"move (\d+) from (\d+) to (\d+)")  # regex pattern for move lines

# loop through moves
for line in move_lines:
    # match the pattern
    match = pattern.match(line)
    # get the number, from, and to
    num = int(match.group(1))
    frm = int(match.group(2)) - 1
    to = int(match.group(3)) - 1
    # do move
    for i in range(num):
        stacks[to].append(stacks[frm].pop())

print("Part 1: ", "".join(stacks[i][-1] for i in range(stack_qty)))


# part 2
stacks = get_initial_stacks(stacks_lines)  # reset stacks lists

for line in move_lines:
    # match the pattern
    match = pattern.match(line)
    # get the number, from, and to
    num = int(match.group(1))
    frm = int(match.group(2)) - 1
    to = int(match.group(3)) - 1
    # do move
    to_move = stacks[frm][-num:]
    stacks[frm] = stacks[frm][:-num]
    stacks[to] = stacks[to] + to_move

print("Part 2: ", "".join(stacks[i][-1] for i in range(stack_qty)))
