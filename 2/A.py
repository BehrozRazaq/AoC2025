data = """"""
intervalls = [interval.split("-") for interval in data.split(",")]
sum = 0
for interval in intervalls:
    interval = range(int(interval[0]), int(interval[1]) + 1)
    for pos in interval:
        pos = str(pos)
        size = len(pos)
        if size % 2 == 1:
            continue
        l, r = pos[: int(size / 2)], pos[int(size / 2) :]
        if l == r:
            sum += int(pos)
print(sum)
