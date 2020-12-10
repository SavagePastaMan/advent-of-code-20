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
    o, t = 0, 0
    for a, b in zip(L, L[1:]):
        if b - a == 1:
            o += 1
        elif b - a == 3:
            t += 1

    return o * t


sdata = sorted([0] + data + [max(data) + 3])
s = set(sdata)

dp = defaultdict(int)
dp[0] = 1


def dfs(n):
    if n == sdata[-1]:
        return dp[n - 1] + dp[n - 2] + dp[n - 3]

    if n - 1 in s:
        dp[n] += dp[n - 1]
    if n - 2 in s:
        dp[n] += dp[n - 2]
    if n - 3 in s:
        dp[n] += dp[n - 3]

    for i in range(1, 4):
        if n + i in s:
            if r := dfs(n + i):
                return r


def part_two():
    return dfs(0)


if __name__ == "__main__":
    # print(part_one())
    print(part_two())
