from typing import List
def parse(data: str) -> List[int]:
    L = [int(x) for x in data.split("\n")]
    return L


def part_one(data: List[int]) -> int:
    s = set()
    for x in data:
        if x not in s:
            s.add(x)
        if 2020 - x in s:
            return (2020 - x) * x


def part_two(data: List[int]) -> int:
    for x in data:
        diff = 2020 - x
        s = set()
        for y in data:
            if y not in s:
                s.add(y)
            if diff - y in s:
                return (diff - y) * y * x


if __name__ == '__main__':
    with open('input.txt') as f:
        problem_input = f.read()

    data = parse(problem_input)

    # print(part_one(data))
    print(part_two(data))
