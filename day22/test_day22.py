from day22_part1 import read_file, step, nth_secret_number, sum_secrets, STEPS
from day22_part2 import get_bananas


def test_step():
    expected = [
        15887950,
        16495136,
        527345,
        704524,
        1553684,
        12683156,
        11100544,
        12249484,
        7753432,
        5908254,
    ]

    number = 123

    while expected:
        next_number = expected.pop(0)
        assert step(number) == next_number
        number = next_number


def test_nth_secret_number():
    n = STEPS
    assert nth_secret_number(1, n) == 8685429
    assert nth_secret_number(10, n) == 4700978
    assert nth_secret_number(100, n) == 15273692
    assert nth_secret_number(2024, n) == 8667524


def test_day22_part1():
    numbers = read_file("day22/test.txt")
    assert sum_secrets(numbers) == 37327623


def test_day22_part2():
    numbers = read_file("day22/test2.txt")
    assert get_bananas(numbers) == 23
