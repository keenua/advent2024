from typing import List, Dict, Set, Tuple, Optional
from dataclasses import dataclass


@dataclass
class Task:
    locks: List[List[int]]
    keys: List[List[int]]


def read_file(file_path: str) -> Task:
    locks: List[List[int]] = []
    keys: List[List[int]] = []

    # read 8 lines at a time
    with open(file_path, "r") as file:
        lines = file.readlines()

        for i in range(0, len(lines), 8):
            data_lines = lines[i : i + 7]
            data = [line.strip() for line in data_lines]
            height = len(data) - 1

            value: List[int] = []

            if data[0] == "#####":
                for x in range(5):
                    for y in range(height):
                        if data[y + 1][x] == ".":
                            value.append(y)
                            break
                locks.append(value)
            else:
                for x in range(5):
                    for y in range(height):
                        if data[height - y - 1][x] == ".":
                            value.append(y)
                            break
                keys.append(value)

    return Task(locks, keys)


def is_fit(lock: List[int], key: List[int]) -> bool:
    for l, k in zip(lock, key):
        if 5 - l < k:
            return False
    return True


def fitting_key_pairs(task: Task) -> int:
    return sum(1 for key in task.keys for lock in task.locks if is_fit(lock, key))


if __name__ == "__main__":
    data = read_file("day25/data.txt")
    print(fitting_key_pairs(data))
