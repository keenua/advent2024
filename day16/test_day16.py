from day16_part1 import read_file, compute_min_score
from day16_part2 import count_tiles_on_best_paths


def test_day16_part1_1():
    grid, start_position, end_position = read_file("day16/test.txt")
    min_score = compute_min_score(grid, start_position, end_position)
    assert min_score == 7036


def test_day16_part1_2():
    grid, start_position, end_position = read_file("day16/test2.txt")
    min_score = compute_min_score(grid, start_position, end_position)
    assert min_score == 11048


def test_day16_part2_1():
    tiles = count_tiles_on_best_paths("day16/test.txt")
    assert tiles == 45


def test_day16_part2_2():
    tiles = count_tiles_on_best_paths("day16/test2.txt")
    assert tiles == 64
