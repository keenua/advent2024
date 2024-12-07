from typing import Counter
from day1_part1 import read_file


def similarity_score(file_path: str) -> int:
    x, y = read_file(file_path)

    y_counter = Counter(y)

    return sum(value * y_counter[value] for value in x)


if __name__ == "__main__":
    print(similarity_score("day1/data.txt"))
