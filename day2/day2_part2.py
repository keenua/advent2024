from typing import List
from day2_part1 import read_file, is_safe

def is_safe_tolerant(row: List[int]) -> bool:
    if is_safe(row):
        return True

    for i in range(len(row)):
        skipped = row[:i] + row[i+1:]
        if is_safe(skipped):
            return True
    
    return False

def count_safe_tolerant(file_path: str) -> int:
    matrix = read_file(file_path)
    return sum(1 for row in matrix if is_safe_tolerant(row))

if __name__ == "__main__":
    print(count_safe_tolerant("day2/data.txt"))

