import helper

data = helper.day(3)


# print(data)


def parse(raw):
    return raw.split("\n")


data = parse(data)


# @helper.timer
def part_one(slopes):
    c = [0 for _ in slopes]
    xs = [0 for _ in slopes]

    for i, row in enumerate(data):
        for n, (dx, dy) in enumerate(slopes):
            if i % dy == 0:
                if row[xs[n]] == "#":
                    c[n] += 1
                xs[n] = (xs[n] + dx) % len(row)

    return c


@helper.timer
def part_two():
    return helper.prod(part_one([(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]))


# print(part_one([(3, 1)]))
print(part_two())

# helper.submit(3, part_one)
# helper.submit(3, part_two)
