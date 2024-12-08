from day8_part1 import count_antidotes, read_file
from day8_part2 import count_resonant_antidotes


def test_count_antidotes():
    data = read_file("day8/test.txt")
    assert count_antidotes(data) == 14


def test_count_resonant_antidotes():
    data = read_file("day8/test.txt")
    assert count_resonant_antidotes(data) == 34
