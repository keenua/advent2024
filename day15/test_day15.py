from day15_part1 import read_input, compute_gps_sum
from day15_part2 import compute_gps_sum_expanded


def test_day15_part1():
    map, moves = read_input("day15/test.txt")
    total_gps = compute_gps_sum(map, moves)
    assert total_gps == 10092


def test_day15_part2():
    map, moves = read_input("day15/test.txt")
    total_gps = compute_gps_sum_expanded(map, moves)
    assert total_gps == 9021
