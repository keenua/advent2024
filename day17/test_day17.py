from day17_part1 import read_file, get_output
from day17_part2 import solve


def test_day17_part1():
    state = read_file("day17/test.txt")
    output = get_output(state)
    assert output == "4,6,3,5,6,3,5,2,1,0"


def test_day17_part2():
    state = read_file("day17/test2.txt")
    assert solve(state.program) == 117440
