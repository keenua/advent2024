from dataclasses import dataclass
from typing import List


@dataclass
class Task:
    test_value: int
    numbers: List[int]


def read_file(file_path: str) -> List[Task]:
    tasks: List[Task] = []

    with open(file_path, "r") as file:
        lines = file.readlines()

        for line in lines:
            l = line.strip()

            if not l:
                continue

            test_value, numbers = l.split(": ")
            tasks.append(
                Task(int(test_value), [int(number) for number in numbers.split(" ")])
            )

    return tasks


def evaluate(
    prev_value: int, test_value: int, numbers: List[int], allow_combine: bool = False
) -> bool:
    if not numbers:
        return prev_value == test_value

    if evaluate(prev_value + numbers[0], test_value, numbers[1:], allow_combine):
        return True

    if evaluate(prev_value * numbers[0], test_value, numbers[1:], allow_combine):
        return True

    if allow_combine:
        return evaluate(
            int(str(prev_value) + str(numbers[0])),
            test_value,
            numbers[1:],
            allow_combine,
        )

    return False


def total_calibration_result(tasks: List[Task], allow_combine: bool = False) -> int:
    total = 0

    for task in tasks:
        if evaluate(0, task.test_value, task.numbers, allow_combine):
            total += task.test_value

    return total


def main():
    tasks = read_file("day7/data.txt")
    print(total_calibration_result(tasks))


if __name__ == "__main__":
    main()
