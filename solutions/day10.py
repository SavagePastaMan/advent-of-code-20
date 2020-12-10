from collections import defaultdict
import helper

data = helper.day(10)


# print(data)

def parse(raw):
    return [int(x) for x in raw.split("\n")]


data = parse(data)


def part_one():
    final = max(data) + 3
    L = [0] + sorted(data) + [final]
    d = defaultdict(int)

    for a, b in zip(L, L[1:]):
        d[b - a] += 1

    return d[1] * d[3]


def part_two():
    t = max(data) + 3
    sdata = sorted([0] + data + [t])
    dp = defaultdict(int)
    dp[0] = 1

    for x in sdata:
        for dx in (1, 2, 3):
            dp[x] += dp[x - dx]

    return dp[t]


if __name__ == "__main__":
    print(part_one())
    print(part_two())
