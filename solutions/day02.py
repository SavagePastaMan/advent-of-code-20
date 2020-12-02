import helper
import re

data = helper.day(2)


def parse(raw):
    pattern = r'(\d+)-(\d+) (\w): (\w+)'
    return re.findall(pattern, raw)


data = parse(data)


@helper.timer
def part_one():
    t = 0
    for a, b, c, s in data:
        x = s.count(c)
        if int(a) <= x <= int(b):
            t += 1
    return t


@helper.timer
def part_two():
    t = 0
    for a, b, c, s in data:
        a = s[int(a) - 1]
        b = s[int(b) - 1]
        t += (a == c) ^ (b == c)

    return t


if __name__ == '__main__':
    print(part_one())
    print(part_two())

    # helper.submit(2, part_one)
    # helper.submit(2, part_two)
