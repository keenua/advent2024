from typing import List, Tuple, Set, Dict
import os

DEBUG = False

Point = Tuple[int, int]
Map = List[List[str]]
DIRECTIONS: Dict[str, Point] = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}


def clear_screen() -> None:
    os.system("cls") if os.name == "nt" else os.system("clear")


def read_input(file_path: str) -> Tuple[Map, str]:
    with open(file_path, "r") as file:
        lines = file.readlines()

    map_lines: Map = []
    move_lines: List[str] = []
    in_moves = False
    map_characters = set("#.@O ")

    for line in lines:
        line = line.rstrip("\n")

        if not line.strip():
            continue

        if not in_moves:
            if all(c in map_characters for c in line):
                map_lines.append(list(line))
            else:
                in_moves = True
                move_lines.append(line)
        else:
            move_lines.append(line)

    move_sequence = "".join(move_lines).replace(" ", "").replace("\n", "")

    return map_lines, move_sequence


def get_robot_pos(map: Map) -> Point:
    for y, line in enumerate(map):
        for x, char in enumerate(line):
            if char == "@":
                return (x, y)

    raise ValueError("Robot not found")


def print_map(
    map: Map,
) -> None:
    for line in map:
        for char in line:
            print(char, end="")
        print()


def is_within_bounds(pos: Point, map: Map) -> bool:
    x, y = pos
    return 0 <= x < len(map[0]) and 0 <= y < len(map)


def simulate_move(map: Map, robot: Point, move: str) -> Tuple[Map, Point]:
    if move not in DIRECTIONS:
        return map, robot

    dx, dy = DIRECTIONS[move]
    rx, ry = (robot[0] + dx, robot[1] + dy)

    if not is_within_bounds((rx, ry), map):
        return map, robot

    if map[ry][rx] == "#":
        return map, robot
    elif map[ry][rx] == "O":
        ex, ey = rx, ry

        while map[ey][ex] == "O" and is_within_bounds((ex, ey), map):
            ex, ey = (ex + dx, ey + dy)

        if not is_within_bounds((ex, ey), map):
            return map, robot

        if map[ey][ex] != ".":
            return map, robot

        map[ey][ex] = "O"

    map[ry][rx] = "@"
    map[robot[1]][robot[0]] = "."
    robot = (rx, ry)

    return map, robot


def simulate_moves(
    map: Map,
    robot: Point,
    move_sequence: str,
) -> Tuple[Map, Point]:
    for move in move_sequence:
        if DEBUG:
            print_map(map)
        map, robot = simulate_move(map, robot, move)
        if DEBUG:
            print(move)
            print_map(map)
            input()
            clear_screen()

    return map, robot


def compute_gps_sum(map: Map, move_sequence: str) -> int:
    robot = get_robot_pos(map)
    map, robot = simulate_moves(map, robot, move_sequence)

    gps_sum = 0
    for y, line in enumerate(map):
        for x, char in enumerate(line):
            if char == "O":
                gps_sum += 100 * y + x

    return gps_sum


if __name__ == "__main__":
    map, move_sequence = read_input("day15/data.txt")
    total_gps = compute_gps_sum(map, move_sequence)
    print(total_gps)
