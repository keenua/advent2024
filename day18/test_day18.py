from day18_part1 import min_steps, read_file
from day18_part2 import first_block


def test_day18_part1():
    data = read_file("day18/test.txt")
    assert min_steps(data, 7, 12) == 22


def test_day18_part2():
    data = read_file("day18/test.txt")
    assert first_block(data, 7) == (6, 1)
