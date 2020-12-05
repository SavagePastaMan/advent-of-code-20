import helper

data = helper.day(5)


def parse(raw):
    return raw.split("\n")


data = parse(data)


def calc_id(st):
    st = st.translate(str.maketrans("RLFB", "1001"))
    return int(st[:7], 2) * 8 + int(st[7:], 2)


def part_one():
    return max(calc_id(x) for x in data)


def part_two():
    s = {calc_id(x) for x in data}
    for i in range(947):
        if i + 1 in s and i - 1 in s and i not in s:
            return i


print(part_one())
print(part_two())


# helper.submit(5, part_one)
# helper.submit(5, part_two)
