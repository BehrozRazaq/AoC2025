data = """"""

from math import ceil


def parse_data(data_pre: str):
    data_post = []
    for line in data.splitlines():
        data_post.append((line.strip()[0], int(line.strip()[1:])))
    return data_post


def traverse_dial(dir, ammount, pos):
    if dir == "L":
        ammount = -ammount
    pos = (pos + ammount) % 100
    return pos


instructions = parse_data(data)
c_pos = 50
n_zero = 0
for turn_dir, number in instructions:
    c_pos = traverse_dial(turn_dir, number, c_pos)
    n_zero += 1 if c_pos == 0 else 0
print(n_zero)
