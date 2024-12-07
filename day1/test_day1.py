from part1 import total_distance
from part2 import similarity_score


def test_part1():
    assert total_distance("day1/test.txt") == 11


def test_part2():
    assert similarity_score("day1/test.txt") == 31
