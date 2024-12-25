from day24_part1 import read_file, compute_task


def test_day24_part1():
    data = read_file("day24/test.txt")
    assert compute_task(data) == 4


def test_day24_part1_2():
    data = read_file("day24/test2.txt")
    assert compute_task(data) == 2024
