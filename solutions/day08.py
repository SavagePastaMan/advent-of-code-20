from __future__ import annotations

import helper

from dataclasses import dataclass
from typing import Tuple, List
from enum import Enum


class Operation(Enum):
    acc = "acc"
    jmp = "jmp"
    nop = "nop"


@dataclass(frozen=True)
class Instruction:
    op: Operation
    arg: int

    @classmethod
    def from_string(cls, string: str) -> Instruction:
        op, arg = string.split(" ")
        return cls(Operation(op), int(arg))

    def unpack(self) -> Tuple[Operation, int]:
        return self.op, self.arg

    def __str__(self):
        return str((self.op, self.arg))


@dataclass
class Application:
    instructions: List[Instruction]
    accumulator: int = 0

    def __enter__(self) -> Application:
        self._original_instructions = self.instructions.copy()
        self._original_accumulator = self.accumulator
        return self

    def __exit__(self, type, value, traceback):
        self.instructions = self._original_instructions
        self.accumulator = self._original_accumulator

    @classmethod
    def from_lines(cls, lines: List[str]):
        return cls(
            [Instruction.from_string(line) for line in lines]
        )

    def run(self) -> int:
        visited = set()
        pointer = 0

        while 0 <= pointer < len(self.instructions):
            inst = self.instructions[pointer]
            op, arg = inst.unpack()

            if pointer in visited:
                break
            visited.add(pointer)

            if op is Operation.acc:
                self.accumulator += arg
                pointer += 1
            elif op is Operation.jmp:
                pointer += arg
            else:
                pointer += 1

        return pointer

    def __str__(self):
        return "\n".join(map(str, self.instructions))


def parse() -> Application:
    data = helper.day(8)

    return Application.from_lines(data.splitlines())


def part_one(app: Application) -> int:
    with app:
        app.run()
        return app.accumulator


def part_two(app: Application) -> int:
    for i, inst in enumerate(app.instructions):
        op, arg = inst.unpack()

        if op is Operation.jmp:
            op = Operation.nop
        elif op is Operation.nop:
            op = Operation.jmp
        else:
            continue

        with app:
            app.instructions[i] = Instruction(op, arg)
            pointer = app.run()

            if pointer == len(app.instructions):
                return app.accumulator


if __name__ == '__main__':
    data = helper.day(8)
    app = Application.from_lines(data.splitlines())

    print(part_one(app))
    print(part_two(app))
