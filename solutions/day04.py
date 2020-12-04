import helper

data = helper.day(4)


# print(data)


def parse(raw):
    data = []
    a = ""
    for x in raw:
        if x.strip():
            a += x
        else:
            data.append(a)
            a = ""
    i = 0
    x = 0
    L = " ".join(data).split("  ")
    # while i < len(data):
    #     if not data[i]:
    #         L.append(" ".join(data[x:i]))
    #         x = i
    #     i += 1
    x = []
    for a in L:
        t = {}
        for b in a.split():
            y = b.split(":")
            t[y[0]] = y[1]
        x.append(t)

    return x


data = parse(data)


# for x in data:
#     print(x)


def part_one():
    f = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    c = 0

    for p in data:
        if all(a in p for a in f):
            c += 1

    return c


def part_two():
    c = 0
    fs = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    for d in data:
        if not all(a in d for a in fs):
            continue

        for f in fs:
            n = False
            if v := d.get(f):
                if f == "byr" and 1920 <= int(v) <= 2002:
                    n = True
                elif f == "iyr" and 2010 <= int(v) <= 2020:
                    n = True
                elif f == "eyr" and 2020 <= int(v) <= 2030:
                    n = True
                elif f == "hcl":
                    if v[0] == "#" and len(v[1:]) == 6 and all(c in "1234567890abcdef" for c in v[1:]):
                        n = True
                elif f == "ecl" and v in ("amb", 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
                    n = True
                elif f == 'pid' and len(v) == 9:
                    try:
                        int(v)
                    except ValueError:
                        pass
                    n = True
                elif f == "hgt":
                    if v[-2:] == 'in':
                        if 59 <= int(v[:-2]) <= 76:
                            c += 1
                    elif v[-2:] == 'cm':
                        if 150 <= int(v[:-2]) <= 193:
                            n = True
            if not n:
                break
        else:
            c += 1
    return c


# print(part_one())
print(part_two())

# helper.submit(4, part_one)
# helper.submit(4, part_two)
