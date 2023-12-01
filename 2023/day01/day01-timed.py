#!/usr/bin/env python3

import re
import time

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


start_time = time.time()
total = get_calibration(puzzle_input)
end_time = time.time()
time_ms = (end_time - start_time) * 1000
print(f"Part 1 total: {total} / Execution time: {time_ms:.2f}ms")

# Part 2
start_time = time.time()
for i, line in enumerate(puzzle_input):
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

total = get_calibration(puzzle_input)
end_time = time.time()
time_ms = (end_time - start_time) * 1000

print(f"Part 2 total: {total} / Execution time: {time_ms:.2f}ms")
