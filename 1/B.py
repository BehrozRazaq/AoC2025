data = """"""

from math import ceil
from tqdm import tqdm


def parse_data(data_pre: str):
    data_post = []
    sum = 0
    for line in data.splitlines():
        amount = int(line.strip()[1:])
        data_post.append((line.strip()[0], amount))
        sum += amount
    return data_post, sum


instructions, sum = parse_data(data)
progress_bar = tqdm(
    total=sum,
)
c_pos = 50
n_zero = 0
for turn_dir, number in instructions:

    for i in range(number):
        if turn_dir == "L":
            c_pos -= 1
        else:
            c_pos += 1
        c_pos %= 100
        if c_pos == 0:
            n_zero += 1
        if i % 100 == 0:
            progress_bar.update(100)
print(n_zero)
