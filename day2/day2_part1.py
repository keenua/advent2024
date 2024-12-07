from typing import List

def read_file(file_path: str) -> List[List[int]]:
    with open(file_path, "r") as file:
        return [list(map(int, line.split())) for line in file.readlines()]

def is_safe(row: List[int]) -> bool:
    if len(row) < 2:
        return True

    increasing = row[0] < row[1]

    for x, y in zip(row, row[1:]):
        if increasing and x > y:
            return False
        elif not increasing and x < y:
            return False

        if not (0 < abs(x - y) < 4):
            return False

    return True

def count_safe(file_path: str) -> int:
    matrix = read_file(file_path)
    return sum(1 for row in matrix if is_safe(row))

if __name__ == "__main__":
    print(count_safe("day2/data.txt"))

