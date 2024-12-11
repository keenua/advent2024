from day11_part1 import count_stones, read_file


if __name__ == "__main__":
    data = read_file("day11/data.txt")
    print(count_stones(data, blinks=75))
