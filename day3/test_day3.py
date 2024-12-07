from day3_part1 import multiply_numbers, read_file
from day3_part2 import multiply_numbers_in_groups


def test_day3_part1():
    assert multiply_numbers(read_file("day3/test_part1.txt")) == 161


def test_day3_part2():
    assert multiply_numbers_in_groups("day3/test_part2.txt") == 48
