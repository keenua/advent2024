from day10_part1 import get_trailheads, read_file
from typing import List, Tuple, Set


def get_trailhead_rating(
    data: List[List[int]], trailhead: Tuple[int, int], prev_value: int = -1
) -> int:
    x, y = trailhead

    if x < 0 or y < 0 or x >= len(data[0]) or y >= len(data):
        return 0

    head_value = data[y][x]

    if head_value != prev_value + 1:
        return 0

    if head_value == 9:
        return 1

    left = get_trailhead_rating(data, (x - 1, y), head_value)
    right = get_trailhead_rating(data, (x + 1, y), head_value)
    up = get_trailhead_rating(data, (x, y - 1), head_value)
    down = get_trailhead_rating(data, (x, y + 1), head_value)

    return left + right + up + down


def get_trailhead_ratings_sum(data: List[List[int]]) -> int:
    return sum(
        get_trailhead_rating(data, trailhead) for trailhead in get_trailheads(data)
    )


if __name__ == "__main__":
    data = read_file("day10/data.txt")
    print(get_trailhead_ratings_sum(data))
