from typing import List

PRUNE_MOD = 16777216
STEPS = 2000


def read_file(file_path: str) -> List[int]:
    with open(file_path, "r") as file:
        return [int(line.strip()) for line in file.readlines()]


def step(number: int) -> int:
    step1 = ((number * 64) ^ number) % PRUNE_MOD
    step2 = ((step1 // 32) ^ step1) % PRUNE_MOD
    step3 = ((step2 * 2048) ^ step2) % PRUNE_MOD
    return step3


def nth_secret_number(initial: int, n: int) -> int:
    for _ in range(n):
        initial = step(initial)
    return initial


def sum_secrets(numbers: List[int], n: int = STEPS) -> int:
    return sum(nth_secret_number(number, n) for number in numbers)


if __name__ == "__main__":
    numbers = read_file("day22/data.txt")
    print(sum_secrets(numbers))
