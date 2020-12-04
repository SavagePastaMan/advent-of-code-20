import re

import helper

data = helper.day(4)
# print(data)


def parse(raw):
    return [
        dict(x.split(':') for x in line.split()) for line in raw.split('\n\n')
    ]


data = parse(data)


def part_one():
    f = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    c = 0

    for p in data:
        c += all(a in p for a in f)

    return c


def part_two():
    c = 0
    fs = {
        'byr': lambda x: 1920 <= int(x) <= 2002,
        'iyr': lambda x: 2010 <= int(x) <= 2020,
        'eyr': lambda x: 2020 <= int(x) <= 2030,
        'hgt': lambda x: (x[-2:] == 'in' and 59 <= int(x[:-2]) <= 76) or (x[-2:] == 'cm' and 150 <= int(x[:-2]) <= 193),
        'hcl': lambda x: bool(re.fullmatch(r'#[0-9a-f]{6}', v)),
        'ecl': lambda x: x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
        'pid': lambda x: x.isdigit() and len(x) == 9
    }

    for p in data:
        for k, cond in fs.items():
            if v := p.get(k):
                if not cond(v):
                    break
            else:
                break
        else:
            c += 1
    return c


# print(part_one())
print(part_two())

# helper.submit(4, part_one)
# helper.submit(4, part_two)
