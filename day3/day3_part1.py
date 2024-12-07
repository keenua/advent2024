import re


def read_file(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.read()


def multiply_numbers(content: str) -> int:
    numbers = re.findall(r"mul\((\d+),(\d+)\)", content)
    return sum(int(a) * int(b) for a, b in numbers)


if __name__ == "__main__":
    print(multiply_numbers(read_file("day3/data.txt")))
