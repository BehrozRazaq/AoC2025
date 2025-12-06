data = """""".splitlines()

problems = [row.split(" ") for row in data]

from math import prod


for row in problems:
    while "" in row:
        row.remove("")

print(problems)
tot_sum = 0
for col in range(len(problems[0])):
    c_problem = []
    for row in range(len(problems)):
        element = problems[row][col]
        if element in ["+", "*"]:
            c_problem.append(element)
            continue
        c_problem.append(int(element))
    match c_problem[-1]:
        case "+":
            res = sum(c_problem[:-1])
        case "*":
            res = prod(c_problem[:-1])
        case _:
            raise ValueError()
    tot_sum += res
print(tot_sum)
