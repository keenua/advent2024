from day9_part1 import defragment, read_file
from day9_part2 import defragment_whole_files


def test_day9_part1():
    data = read_file("day9/test.txt")
    assert defragment(data) == 1928


def test_day9_part2():
    data = read_file("day9/test.txt")
    assert defragment_whole_files(data) == 2858
