#!/usr/bin/env python3

move_score = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}
win_table = {
    "X": {  # Rock
        "A": 3,
        "B": 0,
        "C": 6,
    },
    "Y": {  # Paper
        "A": 6,
        "B": 3,
        "C": 0,
    },
    "Z": {  # Scissors
        "A": 0,
        "B": 6,
        "C": 3,
    },
}

# get input from input.txt file
with open("input.txt") as f:
    puzzle_input = f.readlines()
    puzzle_input = [line.rstrip() for line in puzzle_input]


# part 1
score = 0
for line in puzzle_input:
    opponent_move, my_move = line.split()
    score += move_score[my_move]
    score += win_table[my_move][opponent_move]
print(f"Part 1 Final score: {score}")


# part 2
scoring_table = {
    "A": {
        "X": 3,
        "Y": 1,
        "Z": 2,
    },
    "B": {
        "X": 1,
        "Y": 2,
        "Z": 3,
    },
    "C": {
        "X": 2,
        "Y": 3,
        "Z": 1,
    },
}
win_table = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}
score = 0

for line in puzzle_input:
    opponent_move, strategy = line.split()
    score += win_table[strategy]
    score += scoring_table[opponent_move][strategy]
print(f"Part 2 Final Score: {score}")
