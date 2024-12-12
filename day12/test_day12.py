from day12_part1 import total_price, read_file
from day12_part2 import total_price_with_discount


def test_day12_part1():
    data = read_file("day12/test.txt")
    assert total_price(data) == 1930


def test_day12_part2():
    data = read_file("day12/test.txt")
    assert total_price_with_discount(data) == 1206
