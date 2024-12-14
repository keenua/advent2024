from day14_part1 import read_file, Robot, WIDTH, HEIGHT
from typing import List
from PIL import Image


def move_robots(robots: List[Robot], time: int) -> List[Robot]:
    return [
        Robot(
            (robot.x + robot.dx * time) % WIDTH,
            (robot.y + robot.dy * time) % HEIGHT,
            robot.dx,
            robot.dy,
        )
        for robot in robots
    ]


def get_grid(robots: List[Robot]) -> List[List[str]]:
    grid = [[" " for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for robot in robots:
        grid[robot.y][robot.x] = "#"
    return grid


def print_robots(robots: List[Robot]) -> None:
    grid = get_grid(robots)
    for row in grid:
        print("".join(row))


def write_to_image(robots: List[Robot], filename: str) -> None:
    grid = get_grid(robots)
    image = Image.new("RGB", (WIDTH, HEIGHT))

    for y in range(HEIGHT):
        for x in range(WIDTH):
            image.putpixel((x, y), (0, 255, 0) if grid[y][x] == "#" else (255, 0, 0))
    image.save(f"day14/images/{filename}.png")


if __name__ == "__main__":
    robots = read_file("day14/data.txt")
    for i in range(52, 10000, 103):
        moved_robots = move_robots(robots, i)
        write_to_image(moved_robots, f"grid_{i}")
        print(i)
