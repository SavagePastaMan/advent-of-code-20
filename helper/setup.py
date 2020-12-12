"""Set up solution files"""

from pathlib import Path

FILE_DIR = Path(__file__).parent.parent
TEMPLATE = """\
import helper

data = helper.day({day})


def parse(raw):
    ...


data = parse(data)


def part_one():
    ...


def part_two():
    ...


if __name__ == '__main__':
    print(part_one())
    print(part_two())
"""

for i in range(1, 15):
    file = FILE_DIR / "solutions" / f"day{i:02}.py"
    if file.exists():
        continue

    with open(file, "w") as f:
        f.write(TEMPLATE.format(day=i))
