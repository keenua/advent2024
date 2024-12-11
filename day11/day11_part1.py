from typing import List
from functools import lru_cache


def read_file(file_name: str) -> List[int]:
    with open(file_name, "r") as file:
        return [int(number.strip()) for number in file.read().split()]


@lru_cache(maxsize=None)
def apply_blinks(stone: int, blinks: int) -> int:
    if blinks <= 0:
        return 1

    if stone == 0:
        return apply_blinks(1, blinks - 1)

    str_stone = str(stone)
    if len(str_stone) % 2 == 0:
        left = int(str_stone[: len(str_stone) // 2])
        right = int(str_stone[len(str_stone) // 2 :])

        return apply_blinks(left, blinks - 1) + apply_blinks(right, blinks - 1)

    return apply_blinks(stone * 2024, blinks - 1)


def count_stones(data: List[int], blinks: int = 25) -> int:
    return sum(apply_blinks(stone, blinks) for stone in data)


if __name__ == "__main__":
    data = read_file("day11/data.txt")
    print(count_stones(data))
