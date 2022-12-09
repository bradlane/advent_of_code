#!/usr/bin/env python3


def build_section_set(section):
    # section var should contain a 2 element array with a start and end number
    start, end = section
    return set(range(int(start), int(end) + 1))


# get input from input.txt file
with open("input.txt") as f:
    puzzle_input = f.readlines()
    puzzle_input = [line.rstrip() for line in puzzle_input]


subset_sum = 0
intersect_sum = 0
for line in puzzle_input:
    sections = [item.split("-") for item in line.split(",")]
    section1 = build_section_set(sections[0])
    section2 = build_section_set(sections[1])
    if section1.issubset(section2) or section2.issubset(section1):
        subset_sum += 1

    # part 2
    if section1.intersection(section2) or section2.intersection(section1):
        intersect_sum += 1

print(f"Total sections that are whole subsets: {subset_sum}")
print(f"Total sections that are partial subsets: {intersect_sum}")
