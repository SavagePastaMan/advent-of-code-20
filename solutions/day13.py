import helper

data = helper.day(13)

def parse(raw):
    a, b = raw.split("\n")

    return int(a), [int(x) if x.isdigit() else -1 for x in b.split(",")]


N, data = parse(data)


def part_one():
    L = []
    for x in data:
        t = 0
        if x != -1:
            while t * x <= N:
                t += 1
            L.append(t * x)
        else:
            L.append(10*100)

    return data[L.index(min(L))] * (min(L) - N)


def part_two():
    from sympy.ntheory.modular import crt
    return crt(*zip(*[(x, -i) for i, x in enumerate(data) if x != -1]))[0]


if __name__ == '__main__':
    print(part_one())
    print(part_two())
