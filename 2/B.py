data = """"""
intervalls = [interval.split("-") for interval in data.split(",")]
sum = 0


def check_val(number):
    number = str(number)
    size = len(number)
    sizes = range(2, size + 1)
    for mod in sizes:
        if not (size % mod == 0):
            continue
        delta = int(size / mod)
        divs = [number[i : i + delta] for i in range(0, size, delta)]

        pre = divs[0]

        for div in divs[1:]:
            if not div == pre:
                break
            pre = div
        else:
            return False
    return True


for interval in intervalls:
    interval = range(int(interval[0]), int(interval[1]) + 1)
    for pos in interval:
        if not check_val(pos):
            # print(f"❌❌❌{pos}")
            sum += pos
        # else:
        #    # print(f"✅✅✅{pos}")
print(sum)
