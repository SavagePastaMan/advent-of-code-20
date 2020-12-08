import helper

data = helper.day(8)


# print(data)

def parse(raw):
    L = []
    for x in raw.split("\n"):
        a, b = x.split()
        L.append((a, int(b)))

    return L


data = parse(data)
# print(data)

def part_one():
    v = set()
    acc = 0
    i = 0
    while True:
        if i in v:
            return acc
        v.add(i)
        if data[i][0] == "acc":
            acc += data[i][1]
            i += 1
        elif data[i][0] == "jmp":
            i += data[i][1]
        else:
            i += 1


def is_infinite():
    v = set()
    acc = 0
    i = 0
    while len(v) != len(data):
        if i in v:
            return False
        v.add(i)

        if i == len(data):
            return acc

        if data[i][0] == "acc":
            acc += data[i][1]
            i += 1
        elif data[i][0] == "jmp":
            i += data[i][1]
        else:
            i += 1

    return acc


def part_two():
    for i, x in enumerate(data):
        if x[0] == "nop":
            t = data[i]
            data[i] = ("jmp", x[1])
            if c := is_infinite():
                return c
            data[i] = t
        elif x[0] == "jmp":
            t = data[i]
            data[i] = ("nop", x[1])
            if c := is_infinite():
                return c
            data[i] = t


print(part_one())
print(part_two())

helper.submit(8, part_one)
helper.submit(8, part_two)
