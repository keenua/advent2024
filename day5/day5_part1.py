from dataclasses import dataclass
from typing import List, Tuple, Dict, Optional
from collections import defaultdict


@dataclass
class Task:
    pairs: List[Tuple[int, int]]
    updates: List[List[int]]


def read_file(file_path: str) -> Task:
    pairs = []
    updates = []

    with open(file_path, "r") as file:
        lines = file.readlines()

        pairs_part = True

        for line in lines:
            l = line.strip()

            if pairs_part:
                if l == "":
                    pairs_part = False
                    continue

                pair = tuple(map(int, l.split("|")))
                pairs.append(pair)
            else:
                update = list(map(int, line.split(",")))
                updates.append(update)

    return Task(pairs, updates)


def topological_sort(pairs: List[Tuple[int, int]]) -> Dict[int, int]:
    graph = defaultdict(list)
    nodes = set()

    for first, second in pairs:
        graph[first].append(second)
        nodes.add(first)
        nodes.add(second)

    visited = set()
    temp = set()
    result = []

    def dfs(node, path=[]):
        if node in temp:
            cycle_start = path[path.index(node) :]
            cycle_start.append(node)  # Complete the cycle
            print(f"Cycle detected: {' -> '.join(map(str, cycle_start))}")
            raise ValueError("Graph has a cycle")
        if node in visited:
            return

        temp.add(node)
        path.append(node)

        for neighbor in graph[node]:
            dfs(neighbor, path)

        temp.remove(node)
        path.pop()
        visited.add(node)
        result.append(node)

    for node in nodes:
        if node not in visited:
            dfs(node)

    sorted_pages = result[::-1]

    return {page: index for index, page in enumerate(sorted_pages)}


def get_middle(update: List[int], pages_index: Dict[int, int]) -> Optional[int]:
    for x, y in zip(update, update[1:]):
        if pages_index[x] > pages_index[y]:
            return None
    return update[len(update) // 2]


def get_middle_sum(task: Task) -> int:
    total = 0
    for update in task.updates:
        pairs = [(x, y) for x, y in task.pairs if x in update and y in update]
        pages_index = topological_sort(pairs)
        middle = get_middle(update, pages_index)
        if middle is not None:
            total += middle
    return total


def main():
    task = read_file("day5/data.txt")
    print(get_middle_sum(task))


if __name__ == "__main__":
    main()
