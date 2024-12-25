from day21_part1 import (
    get_dirpad_paths,
    get_numpad_paths,
    get_pad_paths,
    read_file,
    NUMPAD,
    DIRPAD,
    NUMPAD_INDEX,
    DIRPAD_INDEX,
    Point,
)
from typing import Dict, List, Set, Tuple

Matrix = Dict[Tuple[str, int], int]


def split_path(path: str) -> List[str]:
    parts = path.split("A")[:-1]
    return [part + "A" for part in parts]


def convert_path(path: str) -> List[str]:
    assert path[-1] == "A"
    assert "A" not in path[:-1]

    result = []

    prev = "A"
    for c in path:
        paths = get_dirpad_paths(prev, c)
        new_result: List[str] = []

        if not result:
            result = [""]

        for prefix in result:
            for p in paths:
                new_result.append(prefix + p + "A")

        result = new_result
        prev = c

    return result


def get_all_paths(pad: List[List[str]], pad_index: Dict[str, Point]) -> Set[str]:
    result: Set[str] = set()

    for start in pad_index.keys():
        for end in pad_index.keys():
            if start != end and start and end:
                paths = get_pad_paths(start, end, pad, pad_index)
                result.update(paths)

    return result


def build_matrix(steps: int = 2) -> Matrix:
    result: Matrix = {}

    all_paths = get_all_paths(NUMPAD, NUMPAD_INDEX)
    all_paths.update(get_all_paths(DIRPAD, DIRPAD_INDEX))
    all_paths.add("")

    for path in all_paths:
        result[(path + "A", 0)] = len(path) + 1

    for i in range(steps):
        for path in all_paths:
            converted = convert_path(path + "A")
            key = (path + "A", i + 1)

            min_value = float("inf")

            for candidate in converted:
                split = split_path(candidate)

                total = 0

                for part in split:
                    total += result[(part, i)]

                min_value = min(min_value, total)

            result[key] = int(min_value)

    return result


def get_min_presses_dp(code: str, matrix: Matrix, steps: int = 2) -> int:
    presses = 0

    prev = "A"
    for c in code:
        paths = get_numpad_paths(prev, c)
        min_value = float("inf")
        for path in paths:
            min_value = min(min_value, matrix[(path + "A", steps)])
        presses += min_value
        prev = c

    return int(presses)


def get_compexity_dp(code: str, matrix: Matrix, steps: int = 2) -> int:
    numeric_part = int(code.split("A")[0])
    presses = get_min_presses_dp(code, matrix, steps)
    return numeric_part * presses


def get_total_complexity_dp(codes: List[str], steps: int = 2) -> int:
    matrix = build_matrix(steps)
    return sum([get_compexity_dp(code, matrix, steps) for code in codes])


if __name__ == "__main__":
    codes = read_file("day21/data.txt")
    print(get_total_complexity_dp(codes, 25))
