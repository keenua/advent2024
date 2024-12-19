from dataclasses import dataclass
from functools import lru_cache
from typing import List, Dict


@dataclass
class Task:
    towels: List[str]
    patterns: List[str]


@dataclass
class TrieNode:
    children: Dict[str, "TrieNode"]
    is_end_of_word: bool

    def is_towel(self, towel: str) -> bool:
        current = self
        for char in towel:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word


def read_file(file_path: str) -> Task:
    with open(file_path, "r") as file:
        lines = file.readlines()

        towels = lines[0].strip().split(", ")
        patterns: List[str] = []

        for line in lines[2:]:
            patterns.append(line.strip())

        return Task(towels, patterns)


def build_trie(towels: List[str]) -> TrieNode:
    root = TrieNode(children={}, is_end_of_word=False)

    for towel in towels:
        current_node = root
        for char in towel:
            if char not in current_node.children:
                current_node.children[char] = TrieNode(
                    children={}, is_end_of_word=False
                )
            current_node = current_node.children[char]
        current_node.is_end_of_word = True

    return root


class Part1Solver:
    def __init__(self, task: Task):
        self.task = task
        self.trie = build_trie(task.towels)

    @lru_cache(maxsize=None)
    def is_pattern_possible(self, pattern: str, index: int) -> bool:
        for i in range(index, len(pattern)):
            sub = pattern[index : i + 1]
            if self.trie.is_towel(sub):
                if i == len(pattern) - 1:
                    return True
                if self.is_pattern_possible(pattern, i + 1):
                    return True
        return False

    def count_possible_patterns(self) -> int:
        return sum(
            self.is_pattern_possible(pattern, 0) for pattern in self.task.patterns
        )


if __name__ == "__main__":
    task = read_file("day19/data.txt")
    solver = Part1Solver(task)
    print(solver.count_possible_patterns())
