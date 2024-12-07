from day4_part1 import read_file
from typing import List


def safe_eq(content: List[List[str]], x: int, y: int, char: str) -> bool:
    if x < 0 or y < 0 or x >= len(content[0]) or y >= len(content):
        return False
    return content[y][x] == char


def is_mas(content: List[List[str]], x: int, y: int, up_right: bool) -> bool:
    if up_right:
        if safe_eq(content, x - 1, y + 1, "M") and safe_eq(content, x + 1, y - 1, "S"):
            return True
        if safe_eq(content, x - 1, y + 1, "S") and safe_eq(content, x + 1, y - 1, "M"):
            return True
    else:
        if safe_eq(content, x - 1, y - 1, "M") and safe_eq(content, x + 1, y + 1, "S"):
            return True
        if safe_eq(content, x - 1, y - 1, "S") and safe_eq(content, x + 1, y + 1, "M"):
            return True
    return False


def count_x_mas(content: List[List[str]]) -> int:
    total = 0
    for x in range(len(content[0])):
        for y in range(len(content)):
            if content[y][x] == "A":
                if is_mas(content, x, y, True) and is_mas(content, x, y, False):
                    total += 1
    return total


if __name__ == "__main__":
    print(count_x_mas(read_file("day4/data.txt")))
