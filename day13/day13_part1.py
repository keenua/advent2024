from dataclasses import dataclass
from typing import Tuple, List
import re

Point = Tuple[int, int]

@dataclass
class ClawMachine:
    a_button: Point
    b_button: Point
    prize: Point

BUTTON_REGEX = r"Button .: X\+(\d+), Y\+(\d+)"
PRIZE_REGEX = r"Prize: X=(\d+), Y=(\d+)"

MAX_MOVES = 100
MAX_INT = 999999999999999999

def read_point(regex: str, line: str) -> Point:
    match = re.match(regex, line)
    
    if match is None:
        raise ValueError(f"No match found for regex {regex} in line {line}")

    x, y = match.groups()
    return (int(x), int(y))


def read_file(file_path: str) -> List[ClawMachine]:
    with open(file_path, "r") as file:
        lines = file.readlines()

    machines: List[ClawMachine] = []

    for i in range(0, len(lines), 4):
        a_button = read_point(BUTTON_REGEX, lines[i])
        b_button = read_point(BUTTON_REGEX, lines[i + 1])
        prize = read_point(PRIZE_REGEX, lines[i + 2])

        machines.append(ClawMachine(a_button, b_button, prize))

    return machines


def get_machine_tokens(machine: ClawMachine, a_moves = MAX_MOVES, b_moves = MAX_MOVES) -> int:
    ax, ay = machine.a_button
    bx, by = machine.b_button
    px, py = machine.prize

    max_b = min([px // bx, py // by, b_moves])

    result = MAX_INT

    for b in range(max_b, -1, -1):
        x = px - b * bx
        y = py - b * by

        if x % ax != 0 or y % ay != 0:
            continue

        a = x // ax

        if a != y // ay:
            continue

        if a > a_moves:
            continue

        result = min(result, a * 3 + b)

    if result == MAX_INT:
        return 0

    return result


def get_min_tokens(machines: List[ClawMachine]) -> int:
    return sum(get_machine_tokens(machine) for machine in machines)

if __name__ == "__main__":
    machines = read_file("day13/data.txt")
    print(get_min_tokens(machines))
