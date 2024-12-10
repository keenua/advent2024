from typing import List, Tuple, Set


def read_file(file_path: str) -> List[List[int]]:
    with open(file_path, "r") as file:
        return [
            [int(c) if c != "." else -1 for c in line.strip()]
            for line in file.readlines()
        ]


def get_trailheads(data: List[List[int]]) -> List[Tuple[int, int]]:
    heads: List[Tuple[int, int]] = []

    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == 0:
                heads.append((x, y))

    return heads


def get_reachable_nines(
    data: List[List[int]], trailhead: Tuple[int, int], prev_value: int = -1
) -> Set[Tuple[int, int]]:
    x, y = trailhead

    if x < 0 or y < 0 or x >= len(data[0]) or y >= len(data):
        return set()

    head_value = data[y][x]

    if head_value != prev_value + 1:
        return set()

    if head_value == 9:
        return {(x, y)}

    left = get_reachable_nines(data, (x - 1, y), head_value)
    right = get_reachable_nines(data, (x + 1, y), head_value)
    up = get_reachable_nines(data, (x, y - 1), head_value)
    down = get_reachable_nines(data, (x, y + 1), head_value)

    return left | right | up | down


def get_trailhead_score_sum(data: List[List[int]]) -> int:
    heads = get_trailheads(data)
    return sum(len(get_reachable_nines(data, head)) for head in heads)


if __name__ == "__main__":
    data = read_file("day10/data.txt")
    print(get_trailhead_score_sum(data))
