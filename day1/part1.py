from typing import List, Tuple


def read_file(file_path: str) -> Tuple[List[int], List[int]]:
    with open(file_path, "r") as file:
        lines = file.readlines()
        x, y = tuple(
            zip(*[(int(x), int(y)) for x, y in (line.split() for line in lines)])
        )
        return list(x), list(y)


def total_distance(file_path: str) -> int:
    x, y = read_file(file_path)
    x = sorted(x)
    y = sorted(y)

    return sum([abs(x[i] - y[i]) for i in range(len(x))])


if __name__ == "__main__":
    print(total_distance("day1/data.txt"))
