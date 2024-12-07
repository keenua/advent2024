from typing import List


def read_file(file_path: str) -> List[List[str]]:
    with open(file_path, "r") as file:
        return [list(line.strip()) for line in file.readlines()]


def is_xmas(content: List[str]) -> bool:
    return "".join(content) == "XMAS"


def count_xmas(content: List[List[str]]) -> int:
    total = 0

    for x in range(len(content[0])):
        for y in range(len(content)):
            if content[y][x] == "X":
                # horizontal right
                if is_xmas(content[y][x : x + 4]):
                    total += 1
                # horizontal left
                if x - 3 >= 0 and is_xmas(list(reversed(content[y][x - 3 : x + 1]))):
                    total += 1
                # vertical down
                if y + 3 < len(content) and is_xmas(
                    [content[y + i][x] for i in range(4)]
                ):
                    total += 1
                # vertical up
                if y - 3 >= 0 and is_xmas([content[y - i][x] for i in range(4)]):
                    total += 1
                # diagonal down right
                if (
                    y + 3 < len(content)
                    and x + 3 < len(content[0])
                    and is_xmas([content[y + i][x + i] for i in range(4)])
                ):
                    total += 1
                # diagonal up left
                if (
                    y - 3 >= 0
                    and x - 3 >= 0
                    and is_xmas([content[y - i][x - i] for i in range(4)])
                ):
                    total += 1
                # diagonal up right
                if (
                    y - 3 >= 0
                    and x + 3 < len(content[0])
                    and is_xmas([content[y - i][x + i] for i in range(4)])
                ):
                    total += 1
                # diagonal down left
                if (
                    y + 3 < len(content)
                    and x - 3 >= 0
                    and is_xmas([content[y + i][x - i] for i in range(4)])
                ):
                    total += 1
    return total


if __name__ == "__main__":
    print(count_xmas(read_file("day4/data.txt")))
