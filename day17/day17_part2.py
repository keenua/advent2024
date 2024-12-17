from day17_part1 import read_file
from typing import List


def combo_operand(operand: int) -> str:
    if operand <= 3:
        return str(operand)
    elif operand == 4:
        return "a"
    elif operand == 5:
        return "b"
    elif operand == 6:
        return "c"
    else:
        raise ValueError(f"Invalid operand: {operand}")


def instruction(opcode: int, operand: int) -> str:
    if opcode == 0:
        return f"a = a // (2 ** {combo_operand(operand)})"
    elif opcode == 1:
        return f"b ^= {operand}"
    elif opcode == 2:
        return f"b = {combo_operand(operand)} % 8"
    elif opcode == 3:
        raise ValueError(f"JNZ instruction not supported")
    elif opcode == 4:
        return f"b ^= c"
    elif opcode == 5:
        return f"result = {combo_operand(operand)} % 8"
    elif opcode == 6:
        return f"b = a // (2 ** {combo_operand(operand)})"
    elif opcode == 7:
        return f"c = a // (2 ** {combo_operand(operand)})"
    else:
        raise ValueError(f"Invalid opcode: {opcode}")


def program_to_python(program: list[int]) -> str:
    result = ""
    for i in range(0, len(program), 2):
        result += instruction(program[i], program[i + 1]) + "\n"
    return result


def evaluate(program: list[int], a: int) -> int:
    program_str = program_to_python(program[:-2])

    result = 0
    scope = {"a": a, "b": 0, "c": 0, "result": result}
    exec(program_str, scope, scope)
    return scope["result"]


def find(program: List[int], a: int, result: List[int], index: int):
    if evaluate(program, a) != program[-index - 1]:
        return

    if index == len(program) - 1:
        result.append(a)
    else:
        for b in range(8):
            find(program, a * 8 + b, result, index + 1)


def solve(program: List[int]) -> int:
    result = []
    for a in range(8):
        find(program, a, result, 0)
    return result[0]


if __name__ == "__main__":
    state = read_file("day17/data.txt")
    print(solve(state.program))
