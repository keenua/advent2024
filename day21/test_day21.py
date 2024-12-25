from day21_part1 import (
    get_total_complexity,
    read_file,
)
from day21_part2 import get_total_complexity_dp


def test_day21_part1():
    codes = read_file("day21/test.txt")
    assert get_total_complexity(codes) == 126384


def test_day21_part2():
    codes = read_file("day21/test.txt")
    assert get_total_complexity_dp(codes) == 126384
