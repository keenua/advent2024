from typing import List, Dict, Set, Tuple
from dataclasses import dataclass
from collections import defaultdict


@dataclass
class Operation:
    left: str
    right: str
    operation: str
    output: str

    def operands(self) -> Set[str]:
        return set({self.left, self.right})


@dataclass
class Task:
    inputs: Dict[str, bool]
    operations: Dict[str, Operation]


def topological_sort(pairs: List[Tuple[str, str]]) -> List[str]:
    graph = defaultdict(list)
    nodes = set()

    for first, second in pairs:
        graph[first].append(second)
        nodes.add(first)
        nodes.add(second)

    visited = set()
    temp = set()
    result: List[str] = []

    def dfs(node: str, path: List[str] = []):
        if node in temp:
            cycle_start = path[path.index(node) :]
            cycle_start.append(node)
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

    return result[::-1]


def read_file(file_path: str) -> Task:
    inputs: Dict[str, bool] = {}
    operations: Dict[str, Operation] = {}

    with open(file_path, "r") as file:
        for line in file.readlines():
            line = line.strip()

            if not line:
                continue

            if ":" in line:
                key, value = line.split(": ")
                inputs[key] = value == "1"
            else:
                left, op, right, _, out = line.split(" ")
                operations[out] = Operation(left, right, op, out)

    return Task(inputs, operations)


def get_binary_number(registers: Dict[str, bool], key: str) -> str:
    key_registers = [register for register in registers if register.startswith(key)]
    count = len(key_registers)
    bits = ["0"] * count

    for register in key_registers:
        bits[count - int(register[1:]) - 1] = "1" if registers[register] else "0"

    string = "".join(bits)

    return string


def compute_task_binary(task: Task) -> str:
    registers: Dict[str, bool] = dict(task.inputs)

    pairs: List[Tuple[str, str]] = []
    for operation in task.operations.values():
        pairs.append((operation.left, operation.output))
        pairs.append((operation.right, operation.output))

    order = topological_sort(pairs)

    for key in order:
        if key in task.inputs:
            continue

        operation = task.operations[key]
        left = registers[operation.left]
        right = registers[operation.right]

        if operation.operation == "AND":
            registers[key] = left and right
        elif operation.operation == "OR":
            registers[key] = left or right
        elif operation.operation == "XOR":
            registers[key] = left != right

    z_registers = [register for register in registers if register.startswith("z")]
    count = len(z_registers)
    bits = ["0"] * count

    for register in z_registers:
        bits[count - int(register[1:]) - 1] = "1" if registers[register] else "0"

    string = "".join(bits)
    return string


def compute_task(task: Task) -> int:
    return int(compute_task_binary(task), 2)


if __name__ == "__main__":
    data = read_file("day24/data.txt")
    print(compute_task(data))
