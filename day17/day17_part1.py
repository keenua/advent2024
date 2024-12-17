from typing import List, Optional
from dataclasses import dataclass


@dataclass
class State:
    a: int
    b: int
    c: int
    program: List[int]
    pointer: int


def read_file(file_path: str) -> State:
    with open(file_path, "r") as file:
        lines = [line.rstrip("\n") for line in file]
        a = int(lines[0].split(": ")[1])
        b = int(lines[1].split(": ")[1])
        c = int(lines[2].split(": ")[1])
        program = [int(x) for x in lines[4].split(": ")[1].split(",")]
        pointer = 0
        return State(a, b, c, program, pointer)


def combo_operand(state: State, operand: int) -> int:
    if operand <= 3:
        return operand
    elif operand == 4:
        return state.a
    elif operand == 5:
        return state.b
    elif operand == 6:
        return state.c
    else:
        raise ValueError(f"Invalid operand: {operand}")


def op_adv(state: State, operand: int) -> Optional[int]:
    numerator = state.a
    denominator = 2 ** combo_operand(state, operand)
    state.a = numerator // denominator
    state.pointer += 2


def op_bxl(state: State, operand: int) -> Optional[int]:
    state.b = state.b ^ operand
    state.pointer += 2


def op_bst(state: State, operand: int) -> Optional[int]:
    state.b = combo_operand(state, operand) % 8
    state.pointer += 2


def op_jnz(state: State, operand: int) -> Optional[int]:
    if state.a == 0:
        state.pointer += 2
    else:
        state.pointer = operand


def op_bxc(state: State, operand: int) -> Optional[int]:
    state.b ^= state.c
    state.pointer += 2


def op_out(state: State, operand: int) -> Optional[int]:
    value = combo_operand(state, operand) % 8
    state.pointer += 2
    return value


def op_bdv(state: State, operand: int) -> Optional[int]:
    numerator = state.a
    denominator = 2 ** combo_operand(state, operand)
    state.b = numerator // denominator
    state.pointer += 2


def op_cdv(state: State, operand: int) -> Optional[int]:
    numerator = state.a
    denominator = 2 ** combo_operand(state, operand)
    state.c = numerator // denominator
    state.pointer += 2


def execute_instruction(state: State, instruction: int, operand: int) -> Optional[int]:
    if instruction == 0:
        return op_adv(state, operand)
    elif instruction == 1:
        return op_bxl(state, operand)
    elif instruction == 2:
        return op_bst(state, operand)
    elif instruction == 3:
        return op_jnz(state, operand)
    elif instruction == 4:
        return op_bxc(state, operand)
    elif instruction == 5:
        return op_out(state, operand)
    elif instruction == 6:
        return op_bdv(state, operand)
    elif instruction == 7:
        return op_cdv(state, operand)
    else:
        raise ValueError(f"Invalid instruction: {instruction}")


def run_program(state: State, output: List[int]) -> State:
    while state.pointer < len(state.program):
        instruction = state.program[state.pointer]
        operand = state.program[state.pointer + 1]
        result = execute_instruction(state, instruction, operand)
        if result is not None:
            output.append(result)
    return state


def get_output(state: State) -> str:
    output: List[int] = []
    run_program(state, output)
    return ",".join(str(x) for x in output)


if __name__ == "__main__":
    state = read_file("day17/data.txt")
    output = get_output(state)
    print(output)
