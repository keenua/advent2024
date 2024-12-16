from day15_part1 import (
    read_input,
    DIRECTIONS,
    Point,
    Map,
    get_robot_pos,
    print_map,
    is_within_bounds,
    clear_screen,
)
from typing import List, Tuple, Optional

DEBUG = False


def expand_map(map_lines: Map) -> Map:
    result: Map = []

    for line in map_lines:
        new_line: List[str] = []

        for char in line:
            if char == "#":
                new_line += ["#", "#"]
            elif char == "O":
                new_line += ["[", "]"]
            elif char == ".":
                new_line += [".", "."]
            elif char == "@":
                new_line += ["@", "."]

        result.append(new_line)

    return result


def shift(
    map: Map,
    pos: Point,
    direction: Point,
    dp: List[List[Optional[bool]]],
    check_other: bool = True,
) -> bool:
    px, py = pos

    saved = dp[py][px]
    if saved is not None:
        return saved

    dx, dy = direction

    nx, ny = (px + dx, py + dy)

    if not is_within_bounds((nx, ny), map):
        dp[py][px] = False
        return False

    if map[ny][nx] == "#":
        dp[py][px] = False
        return False

    is_horizontal = dx != 0

    if is_horizontal:
        if map[ny][nx] == "." or shift(map, (nx, ny), direction, dp):
            map[ny][nx] = map[py][px]
            map[py][px] = "."
            dp[py][px] = True
            return True
        else:
            dp[py][px] = False
            return False
    else:
        if check_other:
            if map[py][px] == "[":
                if not shift(map, (px + 1, py), direction, dp, check_other=False):
                    dp[py][px] = False
                    return False
            elif map[py][px] == "]":
                if not shift(map, (px - 1, py), direction, dp, check_other=False):
                    dp[py][px] = False
                    return False

        if map[ny][nx] == "." or shift(map, (nx, ny), direction, dp):
            map[ny][nx] = map[py][px]
            map[py][px] = "."
            dp[py][px] = True
            return True
        else:
            dp[py][px] = False
            return False


def simulate_move(map: Map, move: str, robot: Point) -> Tuple[Map, Point]:
    if move not in DIRECTIONS:
        return map, robot

    dx, dy = DIRECTIONS[move]
    nx, ny = (robot[0] + dx, robot[1] + dy)

    height = len(map)
    width = len(map[0])

    dp: List[List[Optional[bool]]] = [[None] * width for _ in range(height)]
    new_map = [line[:] for line in map]

    if shift(new_map, robot, (dx, dy), dp):
        return new_map, (nx, ny)

    return map, robot


def simulate_moves(map: Map, robot: Point, move_sequence: str) -> Tuple[Map, Point]:
    for move in move_sequence:
        if DEBUG:
            print_map(map)

        map, robot = simulate_move(map, move, robot)

        if DEBUG:
            print(move)
            print_map(map)
            input()
            clear_screen()

    if DEBUG:
        clear_screen()
        print_map(map)
        input("DONE?")

    return map, robot


def compute_gps_sum_expanded(map: Map, move_sequence: str) -> int:
    map = expand_map(map)
    robot = get_robot_pos(map)
    map, robot = simulate_moves(map, robot, move_sequence)

    gps_sum = 0
    for y, line in enumerate(map):
        for x, char in enumerate(line):
            if char == "[":
                gps_sum += 100 * y + x

    return gps_sum


if __name__ == "__main__":
    map, moves = read_input("day15/data.txt")
    total_gps = compute_gps_sum_expanded(map, moves)
    print(total_gps)
