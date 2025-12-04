data = """""".split("\n")


def count_neighbours(i, j):
    i_list = set([max(0, i - 1), i, min(i + 1, len(data) - 1)])
    j_list = set([max(0, j - 1), j, min(j + 1, len(data[0]) - 1)])
    sum = 0
    for row_i in i_list:
        for col_i in j_list:
            if row_i == i and col_i == j:
                continue
            if data[row_i][col_i] == "@":
                sum += 1
    return sum


valid_rolls = 0
for row in range(len(data)):
    for col in range(len(data[row])):
        if data[row][col] == "@":
            n_neighbours = count_neighbours(row, col)
            if n_neighbours < 4:
                valid_rolls += 1
print(valid_rolls)
