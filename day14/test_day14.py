from day14_part1 import read_file, compute_safety_factor


def test_day14_part1():
    robots = read_file("day14/test.txt")
    safety_factor = compute_safety_factor(robots, width=11, height=7)
    assert safety_factor == 12
