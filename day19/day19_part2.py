from day19_part1 import Task, build_trie, read_file
from functools import lru_cache


class Part2Solver:
    def __init__(self, task: Task):
        self.task = task
        self.trie = build_trie(task.towels)

    @lru_cache(maxsize=None)
    def count_ways(self, pattern: str, index: int) -> int:
        result = 0

        for i in range(index, len(pattern)):
            sub = pattern[index : i + 1]
            if self.trie.is_towel(sub):
                if i == len(pattern) - 1:
                    result += 1
                else:
                    result += self.count_ways(pattern, i + 1)
        return result

    def sum_ways(self) -> int:
        return sum(self.count_ways(pattern, 0) for pattern in self.task.patterns)


if __name__ == "__main__":
    task = read_file("day19/data.txt")
    solver = Part2Solver(task)
    print(solver.sum_ways())
