from typing import Dict, List, Tuple, Set
import itertools


def read_file(file_path: str) -> List[List[str]]:
    with open(file_path, "r") as file:
        return [list(line.strip()) for line in file.readlines()]


def build_location_map(data: List[List[str]]) -> Dict[str, Set[Tuple[int, int]]]:
    location_map: Dict[str, Set[Tuple[int, int]]] = {}

    for row_index, row in enumerate(data):
        for column_index, cell in enumerate(row):
            if cell != ".":
                if cell not in location_map:
                    location_map[cell] = set()
                location_map[cell].add((row_index, column_index))

    return location_map


def get_antidote_locations(
    size: Tuple[int, int], positions: Set[Tuple[int, int]]
) -> Set[Tuple[int, int]]:
    antidote_locations: Set[Tuple[int, int]] = set()

    w, h = size

    for a, b in itertools.combinations(positions, 2):
        dx, dy = b[0] - a[0], b[1] - a[1]

        if 0 <= b[0] + dx < w and 0 <= b[1] + dy < h:
            antidote_locations.add((b[0] + dx, b[1] + dy))

        if 0 <= a[0] - dx < w and 0 <= a[1] - dy < h:
            antidote_locations.add((a[0] - dx, a[1] - dy))

    return antidote_locations


def count_antidotes(data: List[List[str]]) -> int:
    location_map = build_location_map(data)
    size = (len(data[0]), len(data))

    all_antidotes: Set[Tuple[int, int]] = set()

    for location in location_map.values():
        antidote_locations = get_antidote_locations(size, location)
        all_antidotes.update(antidote_locations)

    return len(all_antidotes)


def main():
    data = read_file("day8/data.txt")
    print(count_antidotes(data))


if __name__ == "__main__":
    main()
