"""Set up solution files"""

from pathlib import Path

FILE_DIR = Path(__file__).parent.parent
TEMPLATE = """\
import helper

data = helper.day({day})


def parse(raw):
    pass

data = parse(data)

def part_one():
    pass


def part_two():
    pass


print(part_one())
print(part_two())

helper.submit({day}, part_one)
helper.submit({day}, part_two)
"""

for i in range(1, 5):
    file = FILE_DIR / "solutions" / f"day{i:02}.py"
    if file.exists():
        continue

    with open(file, "w") as f:
        f.write(TEMPLATE.format(day=i))
