from day1_part1 import total_distance
from day1_part2 import similarity_score


def test_day1_part1():
    assert total_distance("day1/test.txt") == 11


def test_day1_part2():
    assert similarity_score("day1/test.txt") == 31
