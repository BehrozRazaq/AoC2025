LEFT, RIGHT, DOWN = (1, -1), (1, 1), (1, 0)


def add(pos: tuple[int, int], vect: tuple[int, int]) -> tuple[int, int]:
    return pos[0] + vect[0], pos[1] + vect[1]


def fill_grid(data_in: str) -> tuple[dict[tuple[int, int], bool], tuple[int, int]]:
    data = data_in.splitlines()
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


def update_beam(beam, grid, size, cache):
    if beam in cache:
        return cache[beam]
    if size == 0:
        return 1

    if add(beam, DOWN) in grid:
        tot = update_beam(add(beam, LEFT), grid, size - 1, cache) + update_beam(
            add(beam, RIGHT), grid, size - 1, cache
        )
    else:
        tot = update_beam(add(beam, DOWN), grid, size - 1, cache)

    cache[beam] = tot
    return tot


def update_beams(
    grid: dict[tuple[int, int], bool], beam: tuple[int, int], size: int
) -> int:
    cache = {}
    tot = update_beam(beam, grid, size, cache)
    return tot


def main():
    data = """"""

    grid, s = fill_grid(data)
    beam = s

    n = update_beams(grid, beam, len(data.splitlines()))
    print(n)


if __name__ == "__main__":
    main()
