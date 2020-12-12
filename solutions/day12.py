import helper

data = helper.day(12)


def parse(raw):
    trans = {"N": 0, "E": 1, "S": 2, "W": 3}
    return [(trans.get(x[0], x[0]), int(x[1:])) for x in raw.splitlines()]


data = parse(data)

change = {
    0: lambda n: (0, n),
    1: lambda n: (n, 0),
    2: lambda n: (0, -n),
    3: lambda n: (-n, 0),
}


def part_one():
    f = 1
    x = 0
    y = 0

    for d, n in data:
        if d == "F":
            dx, dy = change[f](n)
            x, y = x + dx, y + dy
        elif d == "R":
            f = (f + n // 90) % 4
        elif d == "L":
            f = (f - n // 90) % 4
        else:
            dx, dy = change[d](n)
            x, y = x + dx, y + dy

    return abs(x) + abs(y)


def part_two():
    wx, wy = 10, 1
    sx, sy = 0, 0

    rotation = {
        **dict.fromkeys([("L", 90), ("R", 270)], lambda x, y: (-y, x)),
        **dict.fromkeys([("L", 180), ("R", 180)], lambda x, y: (-x, -y)),
        **dict.fromkeys([("L", 270), ("R", 90)], lambda x, y: (y, -x)),
    }

    for inst in data:
        d, n = inst
        if t := change.get(d):
            dx, dy = t(n)
            wx, wy = wx + dx, wy + dy
        elif d == "F":
            sx += wx * n
            sy += wy * n
        else:
            wx, wy = rotation[inst](wx, wy)

    return abs(sx) + abs(sy)


if __name__ == '__main__':
    print(part_one())
    print(part_two())
