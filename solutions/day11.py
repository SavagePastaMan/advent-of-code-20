import helper
import numpy as np

raw = helper.day(11)
# raw = "L.LL.LL.LL\nLLLLLLL.LL\nL.L.L..L..\nLLLL.LL.LL\nL.LL.LL.LL\nL.LLLLL.LL\n..L.L.....\nLLLLLLLLLL\nL.LLLLLL.L\nL.LLLLL.LL"

FLOOR = -1
EMPTY = 0
OCCUPIED = 1


def parse():
    conv = {".": FLOOR, "L": EMPTY}
    return np.array([[conv[c] for c in line] for line in raw.splitlines()])


def find_seats():
    s = set()

    for i in range(Y):
        for j in range(X):
            if GRID[i][j] == EMPTY:
                s.add((i, j))

    return s


GRID = parse()
X = len(GRID[0])
Y = len(GRID)
SEATS = find_seats()
DS = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1)
]


def get_adj(seat):
    L = []
    x, y = seat
    for dx, dy in DS:
        if (x + dx, y + dy) in SEATS:
            L.append((x + dx, y + dy))
    return L


def get_vis(seat):
    L = []

    x, y = seat
    for dx, dy in DS:
        tx, ty = x + dx, y + dy
        while 0 <= tx < Y and 0 <= ty < X and GRID[tx][ty] == FLOOR:
            tx += dx
            ty += dy
        if (tx, ty) in SEATS:
            L.append((tx, ty))
    return L


adj_seats = {}
vis_seats = {}

for s in SEATS:
    adj_seats[s] = get_adj(s)
    vis_seats[s] = get_vis(s)


def adj(seat, occupied, p):
    c = 0

    cache = adj_seats if p == 4 else vis_seats

    for neighbor in cache[seat]:
        if neighbor in occupied:
            c += 1

    return c


def next_state(occupied, empty, n):
    occupy, deoccupy = set(), set()

    for seat in empty:
        if adj(seat, occupied, n) == 0:
            occupy.add(seat)
    for seat in occupied:
        if adj(seat, occupied, n) >= n:
            deoccupy.add(seat)

    return occupy, deoccupy


def solve(n):
    occupied, empty = SEATS.copy(), set()
    while True:
        occupy, deoccupy = next_state(occupied, empty, n)

        if not occupy and not deoccupy:
            break

        occupied = (occupied - deoccupy) | occupy
        empty = (empty - occupy) | deoccupy

    return len(occupied)


def part_one():
    return solve(4)


def part_two():
    return solve(5)


if __name__ == '__main__':
    print(part_one())
    print(part_two())
