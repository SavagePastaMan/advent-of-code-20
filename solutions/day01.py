from typing import List
import helper

raw = helper.day(1)


def parse(data: str) -> List[int]:
    return [int(x) for x in data.split("\n")]


data = parse(raw)


def part_one() -> int:
    s = set()
    for x in data:
        if x not in s:
            s.add(x)
        if 2020 - x in s:
            return (2020 - x) * x


def part_two() -> int:
    for x in data:
        diff = 2020 - x
        s = set()
        for y in data:
            if y not in s:
                s.add(y)
            if diff - y in s:
                return (diff - y) * y * x


print(part_one())
print(part_two())
