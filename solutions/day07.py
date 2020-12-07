import functools
import re

import helper

data = helper.day(7)


def parse(raw):
    data = [(" ".join(line.split()[:2]), re.findall(r'(\d) (\w+ \w+) bag', line)) for line in raw.splitlines()]
    return {line[0]: {part[1]: int(part[0]) for part in line[1]} for line in data}


data = parse(data)


@functools.lru_cache
def contains(key):
    if key == "shiny gold":
        return 1

    for a in data.get(key, ()):
        if contains(a):
            return 1

    return 0


def part_one():
    return sum(contains(key) for key in data) - 1


@functools.lru_cache
def count(key):
    if key not in data:
        return 0

    c = 0
    for k, v in data[key].items():
        c += v * count(k) + v

    return c


def part_two():
    return count("shiny gold")


print(part_one())
print(part_two())

# helper.submit(7, part_one)
# helper.submit(7, part_two)
