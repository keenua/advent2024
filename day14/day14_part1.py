from typing import List
from dataclasses import dataclass

WIDTH = 101
HEIGHT = 103
TIME = 100


@dataclass
class Robot:
    x: int
    y: int
    dx: int
    dy: int


def read_file(file_path: str) -> List[Robot]:
    robots = []
    with open(file_path, "r") as f:
        content = f.read()
        tokens = content.strip().split()
        for i in range(0, len(tokens), 2):
            pos_token = tokens[i]
            vel_token = tokens[i + 1]
            x_str, y_str = pos_token[2:].split(",")
            dx_str, dy_str = vel_token[2:].split(",")

            x = int(x_str)
            y = int(y_str)
            dx = int(dx_str)
            dy = int(dy_str)

            robots.append(Robot(x, y, dx, dy))
    return robots


def compute_safety_factor(
    robots: List[Robot], time: int = TIME, width: int = WIDTH, height: int = HEIGHT
) -> int:
    mid_x = width // 2
    mid_y = height // 2

    quadrant_counts = [0, 0, 0, 0]  # Q1, Q2, Q3, Q4

    for robot in robots:
        new_x = (robot.x + robot.dx * time) % width
        new_y = (robot.y + robot.dy * time) % height

        if new_x == mid_x or new_y == mid_y:
            continue
        elif new_x > mid_x:
            if new_y < mid_y:
                quadrant_counts[0] += 1
            else:
                quadrant_counts[3] += 1
        elif new_x < mid_x:
            if new_y < mid_y:
                quadrant_counts[1] += 1
            else:
                quadrant_counts[2] += 1

    safety_factor = 1
    for count in quadrant_counts:
        safety_factor *= count

    return safety_factor


if __name__ == "__main__":
    robots = read_file("day14/data.txt")
    safety_factor = compute_safety_factor(robots)
    print(safety_factor)
