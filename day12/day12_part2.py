from day12_part1 import read_file, get_regions
from typing import List


def total_price_with_discount(data: List[List[str]]) -> int:
    regions = get_regions(data)

    return sum(region.sides() * region.area() for region in regions)


if __name__ == "__main__":
    data = read_file("day12/data.txt")
    print(total_price_with_discount(data))
