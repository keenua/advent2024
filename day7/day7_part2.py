from day7_part1 import read_file, total_calibration_result


def main():
    tasks = read_file("day7/data.txt")
    print(total_calibration_result(tasks, allow_combine=True))


if __name__ == "__main__":
    main()
