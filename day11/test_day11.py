from day11_part1 import count_stones, read_file


def test_day11_part1():
    data = read_file("day11/test.txt")
    assert count_stones(data) == 55312


if __name__ == "__main__":
    test_day11_part1()
