from day13_part1 import read_file, get_min_tokens
from day13_part2 import get_corrected_min_tokens


def test_day13_part1():
    claw_machines = read_file("day13/test.txt")
    assert get_min_tokens(claw_machines) == 480


def test_day13_part2():
    claw_machines = read_file("day13/test.txt")
    assert get_corrected_min_tokens(claw_machines) == 875318608908


