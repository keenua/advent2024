from typing import List, Tuple
from day9_part1 import read_file


def defragment_whole_files(data: str) -> int:
    counter = 0

    files: List[Tuple[int, int, int]] = []
    holes: List[Tuple[int, int]] = []

    for index, char in enumerate(data):
        n = int(char)
        if index % 2 == 0:
            files.append((index // 2, counter, n))
        else:
            holes.append((counter, n))

        counter += int(char)

    files_to_check = files[1:][::-1]

    result: List[Tuple[int, int, int]] = []

    for f_id, f_start, f_size in files_to_check:
        found = False

        for h_index, (h_start, h_size) in enumerate(holes):
            if f_size <= h_size and h_start < f_start:
                result.append((h_start, f_id, f_size))
                if f_size == h_size:
                    holes.pop(h_index)
                else:
                    holes[h_index] = (h_start + f_size, h_size - f_size)
                found = True
                break

        if not found:
            result.append((f_start, f_id, f_size))

    total = 0

    for start, id, size in result:
        for i in range(start, start + size):
            total += i * id

    return total


def main():
    data = read_file("day9/data.txt")
    print(defragment_whole_files(data))


if __name__ == "__main__":
    main()
