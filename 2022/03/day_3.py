#!/usr/bin/env python3


def get_priority(item_type):
    # convert from set to string
    item_type = "".join(item_type)

    # get ascii code for each letter
    if item_type.islower():
        # subtract 96 from ascii value so "a" is 1, "z" is 26
        return ord(item_type) - 96
    else:
        # subtract 38 from ascii value so "A" is 27, "Z" is 52
        return ord(item_type) - 38


# get input from input.txt file
with open("input.txt") as f:
    puzzle_input = f.readlines()
    puzzle_input = [line.rstrip() for line in puzzle_input]

priority_sum = 0
for line in puzzle_input:
    comprtmt_size = int(len(line) / 2)
    # get intersection of two compartments
    shared_items = set(line[0:comprtmt_size]) & set(line[comprtmt_size:])

    priority_sum += get_priority(shared_items)
print(f"Sum part 1: {priority_sum}")


# part 2
badge_sum = 0
elf_groups = [puzzle_input[i : i + 3] for i in range(0, len(puzzle_input), 3)]
for group in elf_groups:
    badge = set(group[0]) & set(group[1]) & set(group[2])
    badge_sum += get_priority(badge)
print(f"Sum part 2: {badge_sum}")
