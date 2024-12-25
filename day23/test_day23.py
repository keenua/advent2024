from day23_part1 import get_triples, read_file
from day23_part2 import get_password, read_file as read_file2


def test_day23_part1():
    nodes = read_file("day23/test.txt")
    assert len(get_triples(nodes)) == 7


def test_day23_part2():
    nodes = read_file2("day23/test.txt")
    assert get_password(nodes) == "co,de,ka,ta"
