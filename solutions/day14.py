import itertools

import helper

data = helper.day(14)
# data = "mask = 000000000000000000000000000000X1001X\nmem[42] = 100\nmask = 00000000000000000000000000000000X0XX\nmem[26] = 1"

def parse(raw):
    rest = raw.splitlines()
    L = []
    for line in rest:
        if line.startswith("mask"):
            L.append(line.split(" ")[-1])
        else:
            L.append(helper.extract_ints(line))

    return L


data = parse(data)


def part_one():
    mem = {}
    mask = ""
    for inst in data:
        if isinstance(inst, str):
            mask = inst
        else:
            ma, val = inst
            val = bin(val)[2:]
            mem[ma] = int("".join(str(m) if m != "X" else str(v) for m, v in zip(mask, val.rjust(len(mask), "0"))), 2)

    return sum(mem.values())


def part_two():
    mem = {}
    mask = ""
    for inst in data:
        if isinstance(inst, str):
            mask = inst
        else:
            ma, val = inst
            for x in pos_mas(mask, bin(ma)[2:]):
                mem[x] = val

    return sum(mem.values())


def pos_mas(mask, ma):
    mas = set()

    ma = list(str(m) if m != "0" else v for m, v in zip(mask, ma.rjust(len(mask), "0")))

    def gen_ma(i, ma):
        if i == len(ma):
            mas.add(int("".join(ma).rjust(32, "0"), 2))
            return
        elif ma[i] == "X":
            ma[i] = "0"
            gen_ma(i + 1, ma)
            ma[i] = "X"

            ma[i] = "1"
            gen_ma(i + 1, ma)
            ma[i] = "X"
        else:
            gen_ma(i + 1, ma)

    gen_ma(0, ma)

    return mas


if __name__ == '__main__':
    print(part_one())
    print(part_two())
