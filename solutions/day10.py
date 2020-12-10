from collections import defaultdict
from functools import lru_cache
import helper

data = helper.day(10)


def parse(raw):
    t = [int(x) for x in raw.split("\n")]
    t += [0, max(t) + 3]
    return sorted(t)


data = parse(data)


def part_one():
    d = defaultdict(int)

    for a, b in zip(data, data[1:]):
        d[b - a] += 1

    return d[1] * d[3]


@lru_cache(maxsize=3)
def dfs(x):
    if x == len(data) - 1:
        return 1
    return sum(dfs(x + dx) for dx in range(1, min(4, len(data) - x)) if data[x + dx] - data[x] <= 3)


def part_two():
    return dfs(0)


if __name__ == "__main__":
    print(part_one())
    print(part_two())
