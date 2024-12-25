from day24_part1 import Operation, read_file, Task
from typing import List, Optional, Set


def find_op(
    task: Task,
    op: Optional[str] = None,
    operands: Optional[Set[str]] = None,
    output: Optional[str] = None,
) -> Optional[Operation]:
    for operation in task.operations.values():
        if op is not None and operation.operation != op:
            continue

        if operands is not None and operation.operands() & operands != operands:
            continue

        if output is not None and output != operation.output:
            continue

        return operation
    return None


def find_usages(task: Task, variable: str) -> List[Operation]:
    return [
        operation
        for operation in task.operations.values()
        if variable in operation.operands()
    ]


def validate_task(task: Task) -> Set[str]:
    result: Set[str] = set()

    for i in range(1, 45):
        x = f"x{i:02}"
        y = f"y{i:02}"
        z = f"z{i:02}"

        xor_op = find_op(task, "XOR", operands={x, y})
        if xor_op is None:
            raise Exception(f"No XOR operation found for {x} and {y}")

        and_op = find_op(task, "AND", operands={x, y})
        if and_op is None:
            raise Exception(f"No AND operation found for {x} and {y}")

        xor_usages = find_usages(task, xor_op.output)
        xor_usage_ops = {usage.operation for usage in xor_usages}
        if len(xor_usages) != 2 or xor_usage_ops != {"AND", "XOR"}:
            result.add(xor_op.output)

        and_usages = find_usages(task, and_op.output)
        if len(and_usages) != 1 or and_usages[0].operation != "OR":
            result.add(and_op.output)

        z_op = find_op(task, output=z)

        if z_op is None:
            raise Exception(f"No Z operation found for {z}")

        if z_op.operation != "XOR":
            result.add(z)
        elif xor_op.output not in z_op.operands():
            result.add(xor_op.output)
        else:
            other = (z_op.operands() - {xor_op.output}).pop()
            other_op = find_op(task, output=other)

            if other_op and i != 1 and other_op.operation != "OR":
                result.add(other_op.output)

        z_usages = find_usages(task, z_op.output)
        if z_usages:
            result.add(z_op.output)

    for operation in task.operations.values():
        if operation.operation != "XOR":
            continue

        left, right = sorted(operation.operands())

        if left[0] == "x" and right[0] == "y":
            if operation.output[0] == "z" and operation.output != "z00":
                result.add(operation.output)
        elif operation.output[0] != "z":
            result.add(operation.output)

    return result


def get_names(task: Task) -> str:
    errors = sorted(validate_task(task))
    return ",".join(errors)


if __name__ == "__main__":
    task = read_file("day24/data.txt")
    print(get_names(task))
