from dataclasses import dataclass
from typing import List, Tuple, Dict
from heapq import heappush, heappop


Point = Tuple[int, int]
Map = List[List[bool]]
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


@dataclass
class Task:
    map: Map
    start: Point
    end: Point


def parse_input(file_path: str) -> Task:
    map: Map = []
    start: Point = (-1, -1)
    end: Point = (-1, -1)

    with open(file_path, "r") as file:
        for y, line in enumerate(file.readlines()):
            row: List[bool] = []
            for x, char in enumerate(line.strip()):
                if char == "S":
                    start = (x, y)
                elif char == "E":
                    end = (x, y)
                row.append(char != "#")
            map.append(row)

    return Task(map, start, end)


def manhattan_distance(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x1 - x2) + abs(y1 - y2)


def shortest_path(map: Map, start: Point, end: Point) -> List[Point]:
    x_start, y_start = start
    x_end, y_end = end

    heap: List[Tuple[int, int, int, int, List[Point]]] = []
    heappush(
        heap,
        (
            manhattan_distance(x_start, y_start, x_end, y_end),
            0,
            x_start,
            y_start,
            [start],
        ),
    )

    visited: Dict[Point, int] = {}

    while heap:
        estimated_total_cost, total_cost, x, y, path = heappop(heap)

        if (x, y) == end:
            return path

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
                    new_path = path + [(x_new, y_new)]
                    heappush(
                        heap,
                        (new_estimated_cost, new_total_cost, x_new, y_new, new_path),
                    )

    return []


def within_map(map: Map, x: int, y: int) -> bool:
    return 0 <= x < len(map[0]) and 0 <= y < len(map)


def count_cheats(task: Task, min_gain: int = 1, max_distance: int = 2) -> int:
    path = shortest_path(task.map, task.start, task.end)

    result = 0

    for i, point in enumerate(path[:-1]):
        for j, other_point in enumerate(path[i + 1 :]):
            with_cheat = manhattan_distance(*point, *other_point)
            without_cheat = j + 1

            if with_cheat > max_distance:
                continue

            gain = without_cheat - with_cheat

            if gain >= min_gain:
                result += 1

    return result


if __name__ == "__main__":
    task = parse_input("day20/data.txt")
    print(count_cheats(task, 100, 2))
