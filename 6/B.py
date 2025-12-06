data = """""".splitlines()

from math import prod

original = [[char for char in row] for row in data[:-1]]


def rotate(original):
    n = len(original)
    m = len(original[0])
    new_mat = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new_mat[j][n - i - 1] = original[i][j]
    return new_mat


rotated = rotate(original)

rotated = [[char for char in row if char != " "] for row in rotated]
[row.reverse() for row in rotated]

problems = []
c_row = []
for num in rotated:
    if num == []:
        problems.append(c_row)
        c_row = []
        continue
    c_row.append(int("".join(num)))
problems.append(c_row)

ops = [char for char in data[-1].split(" ") if char != ""]

tot_sum = 0
for op, problem in zip(ops, problems):
    match op:
        case "+":
            res = sum(problem)
        case "*":
            res = prod(problem)
        case _:
            raise ValueError()
    tot_sum += res
print(tot_sum)
