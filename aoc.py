"""CLI for timing and submitting solutions"""

import argparse
import time
import importlib
import helper


def get_day(d: str) -> int:
    d = int(d)
    if 1 <= d <= 25:
        return d

    raise ValueError("Invalid day")


def timer(func):
    s = 0
    for _ in range(100):
        start = time.perf_counter()
        func()
        s += time.perf_counter() - start

    mean = s / 100

    units = ["s", "ms", "us", "ns"]
    i = 0
    while mean < 1/(10 ** (i * 3)):
        i += 1
    return f"{mean * (10**(i*3))}{units[i]}"


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("day", help="day to operate on")
    parser.add_argument("-t", "--timer", action="store_true", help="measure runtime of solutions")
    parser.add_argument("-s", "--submit", action="store_true", help="submit solution for checking")
    args = parser.parse_args()

    d = get_day(args.day)
    solution = importlib.import_module(f"solutions.day{d:02}")

    if args.submit:
        helper.submit(d, solution.part_one)
        helper.submit(d, solution.part_two)

    if args.timer:
        print(timer(solution.part_one))
        print(timer(solution.part_two))
    else:
        print(solution.part_one())
        print(solution.part_two())
