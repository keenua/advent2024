from typing import List, Optional
from day6_part1 import State, move, get_current_position, get_all_positions, read_file


def is_loop(content: List[List[str]], state: State) -> bool:
    positions = set()
    current_state: Optional[State] = state

    while current_state is not None:
        current = (current_state.direction, current_state.position)

        if current in positions:
            return True

        positions.add(current)
        current_state = move(content, current_state)

    return False


def count_possible_obstructions(content: List[List[str]]) -> int:
    start = get_current_position(content)
    path = get_all_positions(content)

    total = 0

    for index, position in enumerate(path):
        # print(f"{index}/{len(path)}")

        if position == start.position:
            continue

        new_content = [row[:] for row in content]
        new_content[position[1]][position[0]] = "#"

        if is_loop(new_content, start):
            total += 1

    return total


def main():
    content = read_file("day6/data.txt")
    print(count_possible_obstructions(content))


if __name__ == "__main__":
    main()
