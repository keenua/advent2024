from day4_part1 import count_xmas, read_file
from day4_part2 import count_x_mas


def test_horizontal_right():
    assert count_xmas([["X", "M", "A", "S"]]) == 1


def test_horizontal_left():
    assert count_xmas([["S", "A", "M", "X"]]) == 1


def test_vertical_down():
    assert count_xmas([["X"], ["M"], ["A"], ["S"]]) == 1


def test_vertical_up():
    assert count_xmas([["S"], ["A"], ["M"], ["X"]]) == 1


def test_diagonal_down_right():
    assert (
        count_xmas(
            [
                ["X", ".", ".", "."],
                [".", "M", ".", "."],
                [".", ".", "A", "."],
                [".", ".", ".", "S"],
            ]
        )
        == 1
    )


def test_diagonal_up_left():
    assert (
        count_xmas(
            [
                ["S", ".", ".", "."],
                [".", "A", ".", "."],
                [".", ".", "M", "."],
                [".", ".", ".", "X"],
            ]
        )
        == 1
    )


def test_diagonal_up_right():
    assert (
        count_xmas(
            [
                [".", ".", ".", "S"],
                [".", ".", "A", "."],
                [".", "M", ".", "."],
                ["X", ".", ".", "."],
            ]
        )
        == 1
    )


def test_diagonal_down_left():
    assert (
        count_xmas(
            [
                [".", ".", ".", "X"],
                [".", ".", "M", "."],
                [".", "A", ".", "."],
                ["S", ".", ".", "."],
            ]
        )
        == 1
    )


def test_day4_part1():
    assert count_xmas(read_file("day4/test.txt")) == 18


def test_day4_part2():
    assert count_x_mas(read_file("day4/test.txt")) == 9
