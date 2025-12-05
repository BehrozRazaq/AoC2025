data = """
""".split(
    "\n"
)

ranges = []
for row in data:
    if row == "":
        break

    cringe = row.split("-")
    l, r = int(cringe[0]), int(cringe[1])
    ranges.append((l, r))
    continue


processed_ranges = {}
while True:
    i = 0
    n_sums = 0

    for c_range in ranges:
        j = 0
        if str(i) in processed_ranges:
            i += 1
            continue
        c_lower, c_higher = c_range
        processed_ranges[str(i)] = [c_lower, c_higher]
        for d_range in ranges:
            if d_range == False or i == j:
                j += 1
                continue
            d_lower, d_higher = d_range
            if d_lower >= c_lower and c_higher >= d_higher:
                processed_ranges[str(j)] = False
                n_sums += 1
            elif d_lower >= c_lower and c_higher >= d_lower:
                c_higher = d_higher
                processed_ranges[str(i)][1] = d_higher
                processed_ranges[str(j)] = False
                n_sums += 1
            elif c_higher >= d_higher and d_higher >= c_lower:
                c_lower = d_lower
                processed_ranges[str(i)][0] = d_lower
                processed_ranges[str(j)] = False
                n_sums += 1
            j += 1
        i += 1
    if n_sums == 0:
        break
    ranges = []

    for key, value in processed_ranges.items():
        if not value:
            continue
        ranges.append(value)
    processed_ranges = {}
    n_sums = 0


sum = 0
for cringe in processed_ranges.values():
    sum += cringe[1] - cringe[0] + 1
    print(cringe[0], cringe[1])

print(sum)
