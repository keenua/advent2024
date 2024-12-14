from day13_part1 import read_file, ClawMachine
from typing import List, Optional, Tuple

SHIFT = 10000000000000


def solve_diophantine(
    a1: int, b1: int, c1: int, a2: int, b2: int, c2: int
) -> Optional[Tuple[int, int]]:
    d = a1 * b2 - a2 * b1
    if d == 0:
        return None
    else:
        x = (c1 * b2 - c2 * b1) // d
        y = (a1 * c2 - a2 * c1) // d
        if (c1 * b2 - c2 * b1) % d != 0 or (a1 * c2 - a2 * c1) % d != 0:
            return None
        return x, y


def get_corrected_machine_tokens(machine: ClawMachine) -> int:
    px, py = machine.prize
    px += SHIFT
    py += SHIFT

    ax, ay = machine.a_button
    bx, by = machine.b_button

    solution = solve_diophantine(ax, bx, px, ay, by, py)

    if solution is None:
        return 0

    a_presses, b_presses = solution

    if a_presses < 0 or b_presses < 0:
        return 0

    total_tokens = a_presses * 3 + b_presses * 1
    return total_tokens


def get_corrected_min_tokens(machines: List[ClawMachine]) -> int:
    return sum(get_corrected_machine_tokens(machine) for machine in machines)


if __name__ == "__main__":
    machines = read_file("day13/data.txt")
    print(get_corrected_min_tokens(machines))
