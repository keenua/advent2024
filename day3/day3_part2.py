import re
from typing import List
from day3_part1 import multiply_numbers, read_file


def find_all_matches(pattern: str, content: str) -> List[int]:
    return [match.start() for match in re.finditer(pattern, content)]


def multiply_numbers_in_groups(file_path: str) -> int:
    content = read_file(file_path)
    dos = find_all_matches(r"do\(\)", content)
    donts = find_all_matches(r"don\'t\(\)", content)

    enabled = True
    start = 0
    total = 0

    while True:
        if enabled:
            if not donts:
                return total + multiply_numbers(content[start:])

            while dos and dos[0] < donts[0]:
                dos.pop(0)
            total += multiply_numbers(content[start : donts[0]])
            donts.pop(0)
            enabled = False
        else:
            if not dos:
                return total

            while donts and donts[0] < dos[0]:
                donts.pop(0)

            enabled = True
            start = dos[0]
            dos.pop(0)


if __name__ == "__main__":
    print(multiply_numbers_in_groups("day3/data.txt"))
