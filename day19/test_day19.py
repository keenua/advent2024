from day19_part1 import read_file, Part1Solver, Task
from day19_part2 import Part2Solver


def test_day19_part1():
    task = read_file("day19/test.txt")
    solver = Part1Solver(task)
    assert solver.count_possible_patterns() == 6


def test_day19_part2():
    task = read_file("day19/test.txt")
    solver = Part2Solver(task)
    assert solver.sum_ways() == 16
