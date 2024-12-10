from day10_part1 import get_trailhead_score_sum, read_file
from day10_part2 import get_trailhead_ratings_sum


def test_day10_part1_1():
    data = read_file("day10/test1.txt")
    assert get_trailhead_score_sum(data) == 2


def test_day10_part1_2():
    data = read_file("day10/test2.txt")
    assert get_trailhead_score_sum(data) == 4


def test_day10_part1_3():
    data = read_file("day10/test3.txt")
    assert get_trailhead_score_sum(data) == 3


def test_day10_part1_4():
    data = read_file("day10/test4.txt")
    assert get_trailhead_score_sum(data) == 36


def test_day10_part2_1():
    data = read_file("day10/test1.txt")
    assert get_trailhead_ratings_sum(data) == 2


def test_day10_part2_2():
    data = read_file("day10/test2.txt")
    assert get_trailhead_ratings_sum(data) == 13


def test_day10_part2_3():
    data = read_file("day10/test3.txt")
    assert get_trailhead_ratings_sum(data) == 3


def test_day10_part2_4():
    data = read_file("day10/test4.txt")
    assert get_trailhead_ratings_sum(data) == 81
