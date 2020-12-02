"""CLI for timing and submitting solutions"""

import argparse
import time


def get_day(d: str) -> int:
    d = int(d)
    if 1 <= d <= 25:
        return d

    raise ValueError("Invalid day")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("day", help="day to operate on")
    parser.add_argument("-t", "--timer", action="store_true", help="measure runtime of solutions")
    parser.add_argument("-s", "--submit", action="store_true", help="submit solution for checking")
    args = parser.parse_args()

    d = get_day(args.day)

