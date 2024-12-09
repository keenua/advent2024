from typing import List


def read_file(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.read().strip()


def generate_indices(data: str) -> List[int]:
    result: List[int] = []
    counter = 0

    for index, char in enumerate(data):
        if index % 2 == 0:
            for _ in range(int(char)):
                result.append(counter)
            counter += 1

    return result


def defragment(data: str) -> int:
    indices = generate_indices(data)
    result = 0
    counter = 0

    for index, char in enumerate(data):
        item_to_pop = 0 if index % 2 == 0 else -1
        for _ in range(int(char)):
            if indices:
                result += indices.pop(item_to_pop) * counter
                counter += 1

    return result


if __name__ == "__main__":
    data = read_file("day9/data.txt")
    print(defragment(data))
