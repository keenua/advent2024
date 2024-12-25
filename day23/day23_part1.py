from typing import List, Set, Tuple, Dict, Optional
from dataclasses import dataclass


@dataclass
class Node:
    name: str
    connected: Set[str]

    def add(self, other: str):
        self.connected.add(other)


def read_file(path: str) -> Dict[str, Node]:
    nodes = {}

    with open(path, "r") as f:
        lines = f.read().splitlines()
        for l in lines:
            left, right = l.split("-")
            if left not in nodes:
                nodes[left] = Node(left, set())
            if right not in nodes:
                nodes[right] = Node(right, set())

            nodes[left].add(right)
            nodes[right].add(left)

    return nodes


def get_triples(nodes: Dict[str, Node]) -> Set[Tuple[str, ...]]:
    result: Set[Tuple[str, ...]] = set()

    node_names = list(nodes.keys())
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            left = node_names[i]
            right = node_names[j]

            if right not in nodes[left].connected:
                continue

            overlap = nodes[left].connected.intersection(nodes[right].connected)

            for common in overlap:
                if common[0] != "t" and right[0] != "t" and left[0] != "t":
                    continue

                triple = sorted([left, right, common])
                result.add(tuple(triple))

    return result


if __name__ == "__main__":
    nodes = read_file("day23/data.txt")
    triples = get_triples(nodes)
    print(len(triples))
