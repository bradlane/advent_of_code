#!/usr/bin/env python3

# get input from input.txt file
with open('input.txt') as f:
    puzzle_input = f.readlines()
    puzzle_input = [line.rstrip() for line in puzzle_input]

# sum calories carried by each elf (input is null-delimited) & add sum to list
calorie_sum = 0
elf_calories = []
for x in puzzle_input:
    if x:
        calorie_sum += int(x)
    else:
        elf_calories.append(calorie_sum)
        calorie_sum = 0

# output max value
print(f"Max calories carried by 1 elf: {max(elf_calories)}")


# Part 2
# get elvles with the 3 most calories and calc sum
print(f"Top 3 calories total: {sum(sorted(elf_calories, reverse=True)[0:3])}")