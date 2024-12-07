from day5_part1 import topological_sort, read_file, get_middle_sum
from day5_part2 import get_incorrect_sum


def test_topological_sort():
    task = read_file("day5/test.txt")
    pages_index = topological_sort(task.pairs)

    for x, y in task.pairs:
        assert pages_index[x] < pages_index[y]


def test_day5_part1():
    task = read_file("day5/test.txt")
    assert get_middle_sum(task) == 143


def test_day5_part2():
    task = read_file("day5/test.txt")
    assert get_incorrect_sum(task) == 123
