from collections import Counter
from functools import reduce

MAX_VALUES = Counter({"red": 12, "green": 13, "blue": 14})

p1_total = 0
p2_total = 0

with open("input.txt", "r") as f:
    for game in f:
        game_id, draws = game.strip().split(": ")
        game_id = int(game_id.split(" ")[1])
        # split out individual draws
        draws = [(c.split(" ") for c in d.split(", ")) for d in draws.split("; ")]
        # convert to counters
        draws = [Counter({c[1]: int(c[0]) for c in d}) for d in draws]

        # part 1
        if all(d <= MAX_VALUES for d in draws):
            p1_total += game_id

        # part 2
        min_cubes = Counter()
        for d in draws:
            # union on counters to get min value of each color
            min_cubes |= d

        p2_total += reduce(lambda a, b: a * b, min_cubes.values())

print(f"Part 1: {p1_total}")
print(f"Part 2: {p2_total}")
