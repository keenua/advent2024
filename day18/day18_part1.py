from typing import List, Tuple, Dict
from heapq import heappush, heappop

Point = Tuple[int, int]
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def read_file(file_path: str) -> List[Point]:
    points: List[Point] = []
    with open(file_path, "r") as file:
        for line in file:
            x, y = line.strip().split(",")
            points.append((int(x), int(y)))
    return points


def build_map(points: List[Point], side_length: int, steps: int) -> List[List[bool]]:
    map = [[True for _ in range(side_length)] for _ in range(side_length)]

    for point in points[:steps]:
        x, y = point
        map[y][x] = False

    return map


def manhattan_distance(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x1 - x2) + abs(y1 - y2)


def shortest_path(map: List[List[bool]], start: Point, end: Point) -> int:
    x_start, y_start = start
    x_end, y_end = end

    heap: List[Tuple[int, int, int, int]] = []
    heappush(
        heap, (manhattan_distance(x_start, y_start, x_end, y_end), 0, x_start, y_start)
    )

    visited: Dict[Point, int] = {}

    while heap:
        estimated_total_cost, total_cost, x, y = heappop(heap)

        if (x, y) == end:
            return total_cost

        state = (x, y)
        if state in visited and visited[state] <= total_cost:
            continue

        visited[state] = total_cost

        for dx, dy in DIRECTIONS:
            x_new, y_new = x + dx, y + dy
            if 0 <= x_new < len(map) and 0 <= y_new < len(map[0]):
                if map[y_new][x_new]:
                    new_total_cost = total_cost + 1
                    new_estimated_cost = new_total_cost + manhattan_distance(
                        x_new, y_new, x_end, y_end
                    )
                    heappush(heap, (new_estimated_cost, new_total_cost, x_new, y_new))

    return -1


def min_steps(points: List[Point], side_length: int, steps: int) -> int:
    map = build_map(points, side_length, steps)
    return shortest_path(map, (0, 0), (side_length - 1, side_length - 1))


if __name__ == "__main__":
    data = read_file("day18/data.txt")
    print(min_steps(data, 71, 1024))
