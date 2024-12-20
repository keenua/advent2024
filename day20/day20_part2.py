from day20_part1 import parse_input, count_cheats


if __name__ == "__main__":
    task = parse_input("day20/data.txt")
    print(count_cheats(task, 100, 20))
