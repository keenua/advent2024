from typing import Dict, List, Tuple, Set
import itertools

from day8_part1 import build_location_map, read_file


def get_resonant_antidote_locations(
    size: Tuple[int, int], positions: Set[Tuple[int, int]]
) -> Set[Tuple[int, int]]:
    antidote_locations: Set[Tuple[int, int]] = set()

    w, h = size

    for a, b in itertools.combinations(positions, 2):
        dx, dy = b[0] - a[0], b[1] - a[1]

        x, y = dx, dy
        while True:
            if 0 <= b[0] + x < w and 0 <= b[1] + y < h:
                antidote_locations.add((b[0] + x, b[1] + y))
            else:
                break

            x, y = x + dx, y + dy

        x, y = -dx, -dy
        while True:
            if 0 <= a[0] + x < w and 0 <= a[1] + y < h:
                antidote_locations.add((a[0] + x, a[1] + y))
            else:
                break

            x, y = x - dx, y - dy

    return antidote_locations


def count_resonant_antidotes(data: List[List[str]]) -> int:
    location_map = build_location_map(data)
    size = (len(data[0]), len(data))

    all_antidotes: Set[Tuple[int, int]] = set()

    for location in location_map.values():
        if len(location) > 1:
            all_antidotes.update(location)

        antidote_locations = get_resonant_antidote_locations(size, location)
        all_antidotes.update(antidote_locations)

    return len(all_antidotes)


def visualize_resonant_antidotes(data: List[List[str]]):
    location_map = build_location_map(data)
    size = (len(data[0]), len(data))

    all_antidotes: Set[Tuple[int, int]] = set()

    for location in location_map.values():
        antidote_locations = get_resonant_antidote_locations(size, location)
        all_antidotes.update(antidote_locations)

    for x, y in all_antidotes:
        if data[x][y] == ".":
            data[x][y] = "#"

    for row in data:
        print("".join(row))


if __name__ == "__main__":
    data = read_file("day8/data.txt")
    print(count_resonant_antidotes(data))
