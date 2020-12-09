import helper
from collections import deque

data = helper.day(9)


def parse(raw):
    return [int(x) for x in raw.split()]


data = parse(data)


def find_sum(q, n):
    s = set()
    for x in q:
        if x not in s:
            s.add(x)
        if n - x in s:
            return True
    else:
        return False


def part_one():
    q = deque(maxlen=25)
    for x in data:
        if len(q) < 25:
            q.append(x)
        else:
            if not find_sum(q, x):
                return x
            q.append(x)


def part_two():
    N = 217430975

    i = 0
    while i < len(data):
        s = data[i]

        j = i + 1
        while j < len(data):
            if s == N:
                return min(data[i: j]) + max(data[i: j])

            if s > N or j == len(data) - 1:
                break
            s += data[j]
            j += 1
        i += 1


print(part_one())
print(part_two())

# helper.submit(9, part_one)
# helper.submit(9, part_two)
