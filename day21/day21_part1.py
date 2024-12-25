from typing import List, Tuple, Dict, Set
from functools import lru_cache

Point = Tuple[int, int]
Pad = List[List[str]]
PadIndex = Dict[str, Point]

NUMPAD: Pad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    ["", "0", "A"],
]

DIRPAD: Pad = [
    ["", "^", "A"],
    ["<", "v", ">"],
]


def to_index(pad: Pad) -> PadIndex:
    index: PadIndex = {}
    for y, row in enumerate(pad):
        for x, value in enumerate(row):
            index[value] = (x, y)
    return index


NUMPAD_INDEX: PadIndex = to_index(NUMPAD)


def read_file(file_path: str) -> List[str]:
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]


DIRPAD_INDEX: PadIndex = to_index(DIRPAD)


def get_pad_paths(
    current: str,
    target: str,
    pad: Pad,
    index: PadIndex,
    prefix: str = "",
) -> Set[str]:
    if current == target:
        return {prefix}

    current_point = index[current]
    cx, cy = current_point
    target_point = index[target]

    dx = target_point[0] - cx
    dy = target_point[1] - cy

    result: Set[str] = set()

    x_dir = 1 if dx > 0 else -1
    y_dir = 1 if dy > 0 else -1
    x_symbol = "<" if dx < 0 else ">"
    y_symbol = "^" if dy < 0 else "v"

    skip_horizontal = prefix and prefix[-1] == y_symbol and dy != 0
    skip_vertical = prefix and prefix[-1] == x_symbol and dx != 0

    if dy != 0 and not skip_vertical:
        vertical = pad[cy + y_dir][cx]
        if vertical != "":
            result.update(
                get_pad_paths(
                    vertical, target, pad, index, prefix + y_symbol
                )
            )

    if dx != 0 and not skip_horizontal:
        horizontal = pad[cy][cx + x_dir]
        if horizontal != "":
            result.update(
                get_pad_paths(
                    horizontal, target, pad, index, prefix + x_symbol
                )
            )

    return result


@lru_cache(maxsize=None)
def get_numpad_paths(
    current: str,
    target: str,
) -> Set[str]:
    return get_pad_paths(current, target, NUMPAD, NUMPAD_INDEX)


@lru_cache(maxsize=None)
def get_dirpad_paths(
    current: str,
    target: str,
) -> Set[str]:
    return get_pad_paths(current, target, DIRPAD, DIRPAD_INDEX)


def number_of_changes(path: str) -> int:
    return sum([1 for i in range(len(path) - 1) if path[i] != path[i + 1]])

def calculate_cost_of_change() -> Dict[Tuple[str, str], int]:
    result: Dict[Tuple[str, str], int] = {}

    for start, start_pos in DIRPAD_INDEX.items():
        for end, end_pos in DIRPAD_INDEX.items():
            if start != end:
                result[(start, end)] = abs(start_pos[0] - end_pos[0]) + abs(
                    start_pos[1] - end_pos[1]
                )

    return result


COST_OF_CHANGE = calculate_cost_of_change()

def get_path_cost(path: str) -> int:
    result = 0
    for i in range(len(path) - 1):
        if path[i] != path[i + 1]:
            result += COST_OF_CHANGE[(path[i], path[i + 1])]
    
    result += len(path)
    return result

@lru_cache(maxsize=None)
def get_shortest_dirpad_path(
    current: str,
    target: str,
) -> str:
    paths = get_dirpad_paths(current, target)
    paths = sorted(paths)
    return min(paths, key=lambda p: get_path_cost(p))


@lru_cache(maxsize=None)
def convert_path(path: str) -> str:
    result = ""
    start = "A"
    for c in path:
        result += get_shortest_dirpad_path(start, c)
        result += "A"
        start = c
    return result


def get_min_presses(code: str) -> int:
    result = 0

    prev = "A"
    for c in code:
        min_presses = 999999999999

        paths = get_numpad_paths(prev, c)
        for path in paths:
            path += "A"

            path = convert_path(path)
            path = convert_path(path)
            min_presses = min(min_presses, len(path))

        result += min_presses
        prev = c

    return result


def get_complexity(code: str) -> int:
    numeric_part = int(code.split("A")[0])
    presses = get_min_presses(code)
    return numeric_part * presses


def get_total_complexity(codes: List[str]) -> int:
    return sum([get_complexity(code) for code in codes])


if __name__ == "__main__":
    codes = read_file("day21/data.txt")
    print(get_total_complexity(codes))
