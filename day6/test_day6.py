from day6_part1 import count_distinct_positions, read_file
from day6_part2 import count_possible_obstructions


def test_day6_part1():
    task = read_file("day6/test.txt")
    assert count_distinct_positions(task) == 41


def test_day6_part2():
    task = read_file("day6/test.txt")
    assert count_possible_obstructions(task) == 6
