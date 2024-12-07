from dataclasses import dataclass
from typing import List, Tuple, Optional, Set
from enum import Enum


class Direction(Enum):
    UP = "^"
    DOWN = "v"
    LEFT = "<"
    RIGHT = ">"


@dataclass
class State:
    direction: Direction
    position: Tuple[int, int]


def read_file(file_path: str) -> List[List[str]]:
    with open(file_path, "r") as file:
        return [list(line.strip()) for line in file.readlines()]


def get_current_position(content: List[List[str]]) -> State:
    for y, line in enumerate(content):
        for x, char in enumerate(line):
            if char == "^":
                return State(Direction.UP, (x, y))

    raise ValueError("No starting position found")


def get_next_position(content: List[List[str]], state: State) -> Optional[State]:
    x, y = state.position
    if state.direction == Direction.UP:
        y -= 1
    elif state.direction == Direction.DOWN:
        y += 1
    elif state.direction == Direction.LEFT:
        x -= 1
    elif state.direction == Direction.RIGHT:
        x += 1

    if y < 0 or y >= len(content) or x < 0 or x >= len(content[0]):
        return None

    return State(state.direction, (x, y))


def rotate_direction(direction: Direction) -> Direction:
    if direction == Direction.UP:
        return Direction.RIGHT
    elif direction == Direction.RIGHT:
        return Direction.DOWN
    elif direction == Direction.DOWN:
        return Direction.LEFT
    elif direction == Direction.LEFT:
        return Direction.UP


def move(content: List[List[str]], state: State) -> Optional[State]:
    next_position = get_next_position(content, state)
    if next_position is None:
        return None

    if content[next_position.position[1]][next_position.position[0]] == "#":
        next_position = State(rotate_direction(next_position.direction), state.position)

    return next_position


def get_all_positions(content: List[List[str]]) -> Set[Tuple[int, int]]:
    state = get_current_position(content)
    positions = set()

    while state is not None:
        positions.add(state.position)
        state = move(content, state)

    return positions


def count_distinct_positions(content: List[List[str]]) -> int:
    return len(get_all_positions(content))


def main():
    content = read_file("day6/data.txt")
    print(count_distinct_positions(content))


if __name__ == "__main__":
    main()
