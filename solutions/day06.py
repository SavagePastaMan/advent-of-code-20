import helper

data = helper.day(6)


def parse(raw):
    return raw.split("\n\n")


data = parse(data)


def part_one():
    return sum(len(set(x.replace("\n", ""))) for x in data)


def part_two():
    return sum(len(set.intersection(*[set(n) for n in x.split("\n")])) for x in data)


helper.submit(6, part_one)
helper.submit(6, part_two)
