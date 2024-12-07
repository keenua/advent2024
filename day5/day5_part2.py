from day5_part1 import Task, read_file, get_middle, topological_sort


def get_incorrect_sum(task: Task) -> int:
    total = 0
    for update in task.updates:
        pairs = [(x, y) for x, y in task.pairs if x in update and y in update]
        pages_index = topological_sort(pairs)
        middle = get_middle(update, pages_index)

        if middle is None:
            # sort the update correctly
            update.sort(key=lambda x: pages_index[x])
            total += update[len(update) // 2]
    return total


def main():
    task = read_file("day5/data.txt")
    print(get_incorrect_sum(task))


if __name__ == "__main__":
    main()
