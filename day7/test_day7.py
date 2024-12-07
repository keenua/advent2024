from day7_part1 import evaluate, read_file, total_calibration_result


def test_day7_evaluate():
    assert evaluate(0, 190, [10, 19])


def test_day7_evaluate_combine():
    assert evaluate(0, 119, [1, 19], allow_combine=True)


def test_day7_part1():
    tasks = read_file("day7/test.txt")
    assert total_calibration_result(tasks) == 3749


def test_day7_part2():
    tasks = read_file("day7/test.txt")
    assert total_calibration_result(tasks, allow_combine=True) == 11387
