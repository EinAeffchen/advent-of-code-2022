from pathlib import Path
from numpy import array, rot90
from typing import List
from functools import reduce


def read_input() -> map:
    with open(Path(__file__).parent / "input", "r") as i:
        lines = i.readlines()
        raw_container_state = lines[:8]
        container_rows = array(
            list(
                map(
                    lambda x: [
                        x[:-1][i : i + 4].replace("[", "").replace("]", "").strip()
                        for i in range(0, len(x[:-1]), 4)
                    ],
                    raw_container_state,
                )
            )
        )
        container_matrix = rot90(container_rows, axes=(1, 0)).tolist()
        container_matrix = map(lambda y: list(filter(lambda x: x, y)), container_matrix)
        commands = lines[10:]
        return (list(container_matrix), commands)


def move_n(container_stack: list, n: int):
    for _ in range(n):
        yield container_stack.pop()


def move_n_9001(container_stack: list, n: int):
    stack = []
    for _ in range(n):
        stack.append(container_stack.pop())
    stack.reverse()
    return stack


def process_commands(function):
    matrix, commands = read_input()
    for command in commands:
        amount, position1, position2 = (
            command.strip()
            .replace("move", "")
            .replace("from", "")
            .replace("to", "")
            .split()
        )
        amount = int(amount)
        position1 = int(position1)
        position2 = int(position2)
        matrix[position2 - 1] += function(matrix[position1 - 1], amount)
    for row in matrix:
        print(row[-1])


if __name__ == "__main__":
    print("Part1")
    process_commands(move_n)  # part1
    print("Part2")
    process_commands(move_n_9001)  # part2
