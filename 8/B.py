class Box:
    circuit: "Circuit"

    def __init__(self, pos: tuple[int, int, int]) -> None:
        self.pos = pos

    def set_circuit(self, circuit: "Circuit") -> None:
        self.circuit = circuit

    def get_circuit(self) -> "Circuit|None":
        if self.circuit:
            return self.circuit
        return None

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Box):
            raise ValueError(f"comparing box to {other}")
        return self.pos == other.pos

    def distance(self, other: "Box") -> float:
        return (
            (self.pos[0] - other.pos[0]) ** 2
            + (self.pos[1] - other.pos[1]) ** 2
            + (self.pos[2] - other.pos[2]) ** 2
        ) ** 0.5

    def __str__(self) -> str:
        return str(self.pos)

    def __repr__(self) -> str:
        return f"{str(self.pos)}"


class Circuit:
    def __init__(self, boxes: list[Box]) -> None:
        self.boxes = boxes
        for box in self.boxes:
            box.set_circuit(self)

    def __len__(self) -> int:
        return len(self.boxes)

    def __lt__(self, other) -> bool:
        return len(self) < len(other)

    def __repr__(self) -> str:
        return str(self.boxes)


def parse_boxes(data: str) -> tuple[list[Box], list[Circuit]]:
    boxes: list[Box] = []
    circuits = []
    for line in data.splitlines():
        coords_ls = [int(n) for n in line.split(",")]
        coords = (coords_ls[0], coords_ls[1], coords_ls[2])
        box = Box(coords)
        circuits.append(Circuit([box]))
        boxes.append(box)
    return boxes, circuits


def calc_distances(
    boxes: list[Box], distance_map: dict[float, tuple[Box, Box]]
) -> list[float]:
    res = []
    i = 0
    for l_box in boxes:
        i += 1
        for r_box in boxes[i:]:
            if l_box == r_box:
                continue
            distance = l_box.distance(r_box)
            distance_map[distance] = (l_box, r_box)
            res.append(distance)
    return res


def next_connection(l_box: Box, r_box: Box, circuits: list[Circuit]) -> None:
    l_c, r_c = l_box.circuit, r_box.circuit
    if l_c != r_c:
        circuits.remove(l_c)
        circuits.remove(r_c)
        circuits.append(Circuit(l_c.boxes + r_c.boxes))


def main():
    data = """"""

    boxes, circuits = parse_boxes(data)
    distance_map = {}
    distances = calc_distances(boxes, distance_map)

    distances.sort()
    connection = 0

    while len(circuits) > 1:
        l_box, r_box = distance_map[distances[connection]]
        next_connection(l_box, r_box, circuits)
        connection += 1

    circuits.sort(reverse=False)

    from math import prod

    print(l_box.pos[0] * r_box.pos[0])


if __name__ == "__main__":
    main()
