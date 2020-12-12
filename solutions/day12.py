import helper

data = helper.day(12)
# data = "F10\nN3\nF7\nR90\nF11"


# print(data)

def parse(raw):
    L = []
    for x in raw.split("\n"):
        L.append((x[0], int(x[1:])))
    return L


data = parse(data)


def part_one():
    f = 1
    X = 0
    Y = 0
    for d, n in data:
        if d == "F":
            if f == 0:
                Y += n
            elif f == 1:
                X += n
            elif f == 2:
                Y -= n
            elif f == 3:
                X -= n
        elif d == "R":
            f += n / 90
            f %= 4
        elif d == "L":
            f -= n / 90
            f %= 4
        elif d == "N":
            Y += n
        elif d == "E":
            X += n
        elif d == "S":
            Y -= n
        elif d == "W":
            X -= n

    return abs(X) + abs(Y)


def part_two():
    X, Y = 10, 1

    sx, sy = 0, 0

    for d, n in data:
        if d == "N":
            Y += n
        elif d == "S":
            Y -= n
        elif d == "E":
            X += n
        elif d == "W":
            X -= n
        elif d == "R":
            if n == 180:
                X, Y = -X, -Y
            if n == 90:
                X, Y = Y, -X
            elif n == 270:
                X, Y = -Y, X
        elif d == "L":
            if n == 180:
                X, Y = -X, -Y
            elif n == 90:
                X, Y = -Y, X
            elif n == 270:
                X, Y = Y, -X
        elif d == "F":
            sx += X * n
            sy += Y * n

    return abs(sx) + abs(sy)


if __name__ == '__main__':
    print(part_one())
    print(part_two())
