from typing import List, Tuple
from networkx import Graph, find_cliques

Nodes = List[Tuple[str, str]]


def read_file(path: str) -> Nodes:
    nodes: Nodes = []

    with open(path, "r") as f:
        lines = f.read().splitlines()
        for l in lines:
            left, right = l.split("-")
            nodes.append((left, right))

    return nodes


def get_password(nodes: Nodes) -> str:
    graph = Graph()
    graph.add_edges_from(nodes)

    cliques = list(find_cliques(graph))

    largest = max(cliques, key=len)
    return ",".join(sorted(largest))


if __name__ == "__main__":
    nodes = read_file("day23/data.txt")
    print(get_password(nodes))
