LEFT, RIGHT, DOWN = (1, -1), (1, 1), (1, 0)


def add(pos: tuple[int, int], vect: tuple[int, int]) -> tuple[int, int]:
    return pos[0] + vect[0], pos[1] + vect[1]


def fill_grid(data: str) -> tuple[dict[tuple[int, int]], tuple[int, int]]:
    data = data.splitlines()
    grid = {}
    start = (-1, -1)
    for row in range(len(data)):
        for col in range(len(data[row])):
            char = data[row][col]
            if char == "^":
                grid[(row, col)] = True
            if char == "S":
                start = (row, col)
    return grid, start


def update_beams(
    grid: dict[tuple[int, int]], beams: set[tuple[int, int]]
) -> tuple[set[tuple[int, int]], int]:
    new_beams = set()
    n_splits = 0
    for beam in beams:
        if add(beam, DOWN) in grid:
            new_beams.add(add(beam, LEFT))
            new_beams.add(add(beam, RIGHT))
            n_splits += 1
        else:
            new_beams.add(add(beam, DOWN))
    return new_beams, n_splits


def main():
    data = """"""

    grid, s = fill_grid(data)
    beams = {s}
    n_splits = 0
    for _ in range(len(data.splitlines())):
        beams, c_splits = update_beams(grid, beams)
        n_splits += c_splits
    print(n_splits)


if __name__ == "__main__":
    main()
