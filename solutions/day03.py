import helper

data = helper.day(3)
# print(data)

def parse(raw):
    return raw.split("\n")


data = parse(data)


def part_one(right, down):
    c = 0
    y = 0
    for row in data[::down]:
        if row[y] == "#":
            c += 1
        y = (y + right) % len(row)
    return c


def part_two():
    return part_one(1, 1) * part_one(3, 1) * part_one(5, 1) * part_one(7, 1) * part_one(1, 2)


# print(part_one(3, 1))
print(part_two())

# helper.submit(3, part_one)
helper.submit(3, part_two)
