from day2_part1 import count_safe
from day2_part2 import count_safe_tolerant

def test_day2_part1():
    assert count_safe("day2/test.txt") == 2

def test_day2_part2():
    assert count_safe_tolerant("day2/test.txt") == 4
