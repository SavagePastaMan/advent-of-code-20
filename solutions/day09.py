import helper
from collections import deque

data = helper.day(9)


def parse(raw):
    return [int(x) for x in raw.split()]


data = parse(data)


def part_one():
    q = deque(maxlen=25)
    s = set()
    for x in data:
        if len(q) < 25:
            q.append(x)
            s.add(x)
        else:
            for e in q:
                if x - e in s:
                    break
            else:
                return x
            s.remove(q[0])
            q.append(x)
            s.add(x)


def part_two():
    N = 217430975

    d = deque()
    s = 0

    for x in data:
        s += x
        d.append(x)

        while s > N:
            s -= d.popleft()

        if s == N:
            return min(d) + max(d)


if __name__ == "__main__":
    print(part_one())
    print(part_two())
