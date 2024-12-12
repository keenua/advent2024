from typing import List, Tuple, Set
from dataclasses import dataclass

Point = Tuple[int, int]

MAX_INT = 999999
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def is_edge(point: Point, all_points: Set[Point], direction: Tuple[int, int]) -> bool:
    x, y = point
    dx, dy = direction
    nx, ny = x + dx, y + dy

    return (nx, ny) not in all_points


@dataclass
class Region:
    points: Set[Point]
    char: str

    def perimeter(self) -> int:
        result = 0
        for x, y in self.points:
            for dx, dy in DIRECTIONS:
                if is_edge((x, y), self.points, (dx, dy)):
                    result += 1

        return result

    def area(self) -> int:
        return len(self.points)

    def sides(self) -> int:
        visited: List[Set[Point]] = []
        for _ in range(4):
            visited.append(set())

        count = 0

        for x, y in self.points:
            for di, (dx, dy) in enumerate(DIRECTIONS):
                if (x, y) in visited[di]:
                    continue

                if is_edge((x, y), self.points, (dx, dy)):
                    count += 1

                    if dx == 0:
                        for nx in range(x - 1, -1, -1):
                            if (nx, y) in self.points and is_edge(
                                (nx, y), self.points, (dx, dy)
                            ):
                                visited[di].add((nx, y))
                            else:
                                break
                        for nx in range(x + 1, MAX_INT):
                            if (nx, y) in self.points and is_edge(
                                (nx, y), self.points, (dx, dy)
                            ):
                                visited[di].add((nx, y))
                            else:
                                break
                    else:
                        for ny in range(y - 1, -1, -1):
                            if (x, ny) in self.points and is_edge(
                                (x, ny), self.points, (dx, dy)
                            ):
                                visited[di].add((x, ny))
                            else:
                                break
                        for ny in range(y + 1, MAX_INT):
                            if (x, ny) in self.points and is_edge(
                                (x, ny), self.points, (dx, dy)
                            ):
                                visited[di].add((x, ny))
                            else:
                                break

        return count


def read_file(file_path: str) -> List[List[str]]:
    with open(file_path, "r") as file:
        return [list(line.strip()) for line in file.readlines()]


def get_region(data: List[List[str]], point: Point) -> Region:
    x, y = point
    char = data[y][x]

    visited: Set[Point] = set()

    queue: List[Point] = [point]
    region: Set[Point] = set()

    while queue:
        x, y = queue.pop(0)
        region.add((x, y))

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(data[0]) and 0 <= ny < len(data):
                if data[ny][nx] == char and (nx, ny) not in visited:
                    queue.append((nx, ny))
                    visited.add((nx, ny))

    return Region(points=region, char=char)


def get_regions(data: List[List[str]]) -> List[Region]:
    regions: List[Region] = []
    visited: Set[Point] = set()

    for row_index, row in enumerate(data):
        for column_index, cell in enumerate(row):
            point = (column_index, row_index)

            if point in visited:
                continue

            region = get_region(data, point)
            regions.append(region)

            visited.update(region.points)

    return regions


def total_price(data: List[List[str]]) -> int:
    regions = get_regions(data)

    return sum(region.perimeter() * region.area() for region in regions)


if __name__ == "__main__":
    data = read_file("day12/data.txt")
    print(total_price(data))
