#!/usr/bin/env python3

# https://adventofcode.com/2022/day/6

# get input from input.txt file
with open("input.txt") as f:
    puzzle_input = f.read().rstrip()

# earliest marker can be is at position 4
marker = 4
# loop through individual chars in line
for i in range(len(puzzle_input)):
    packet = puzzle_input[i : i + 4]
    # if length of unique set is 4, all chars unique
    if len(set(packet)) == 4:
        break
    else:
        marker = marker + 1
print(f"First marker: {marker}")


# Part 2
# same as part 1, but message is 14 unique chars
start_of_msg = 14
for i in range(len(puzzle_input)):
    msg = puzzle_input[i : i + 14]
    # if length of unique set is 14, all chars unique
    if len(set(msg)) == 14:
        break
    else:
        start_of_msg = start_of_msg + 1
print(f"Start of message: {start_of_msg}")