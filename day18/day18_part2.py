from typing import List, Optional
from day18_part1 import min_steps, read_file, Point


def first_block(points: List[Point], side_length: int) -> Optional[Point]:
    for steps in range(1, len(points)):
        if min_steps(points, side_length, steps) == -1:
            return points[steps - 1]
    return None


if __name__ == "__main__":
    data = read_file("day18/data.txt")
    print(first_block(data, 71))
