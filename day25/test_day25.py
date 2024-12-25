from day25_part1 import read_file, fitting_key_pairs


def test_day25_part1():
    data = read_file("day25/test.txt")
    assert fitting_key_pairs(data) == 3
