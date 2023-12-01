#!/usr/bin/env python3

import re

with open("input.txt") as f:
    puzzle_input = f.readlines()
    puzzle_input = [line.rstrip() for line in puzzle_input]


# Part 1
def get_calibration(data):
    # pull all digits from each input lines
    digits = [re.findall("\d", line) for line in data]
    # get first and last digit from each line & return sum of all numbers
    nums = [int(n[0] + n[-1]) for n in digits]
    return sum(nums)


print("Part 1 total:", get_calibration(puzzle_input))


# Part 2
for i, line in enumerate(puzzle_input):
    # replace named number strings with digits
    # preserve first and last char of each so we don't have to care about position in
    #   str relative to other potentially valid replacements
    line = (
        line.replace("one", "o1e")
        .replace("two", "t2o")
        .replace("three", "t3e")
        .replace("four", "f4r")
        .replace("five", "f5e")
        .replace("six", "s6x")
        .replace("seven", "s7n")
        .replace("eight", "e8t")
        .replace("nine", "n9e")
    )
    puzzle_input[i] = line

print("Part 2 total:", get_calibration(puzzle_input))
