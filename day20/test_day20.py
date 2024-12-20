from day20_part1 import parse_input, count_cheats


def test_day20_part1():
    task = parse_input("day20/test.txt")
    assert count_cheats(task) == 44


def test_day20_part2():
    task = parse_input("day20/test.txt")
    assert count_cheats(task, 50, 20) == 285
