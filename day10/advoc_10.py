from __future__ import annotations
from pathlib import Path


def read_input() -> map:
    with open(Path(__file__).parent / "input", "r") as i:
        return [row.strip() for row in i.readlines()]


def part1():
    current_value = 1
    status = list()
    signal_points = [20, 60, 100, 140, 180, 220]
    for command in read_input():
        if command == "noop":
            status.append(current_value)
        else:
            value = command.split()[1]
            status.append(current_value)
            status.append(current_value)
            current_value += int(value)

    print(sum([status[point - 1] * point for point in signal_points]))


def write_pixel(cycle: int, register: int):
    break_cycle = 40
    diff = int(cycle / 40)
    allowed_range = list(range(register - 1 + (diff * 40), register + 2 + (diff * 40)))
    if cycle - 1 in allowed_range:
        print("{0: <5}".format("#"), end="")
    else:
        print("{0: <5}".format("."), end="")
    if cycle % break_cycle == 0:
        print("\n")


def part2():
    register = 1
    cycles = 1
    for command in read_input():
        if command == "noop":
            write_pixel(cycles, register)
            cycles += 1
        else:
            write_pixel(cycles, register)
            cycles += 1
            write_pixel(cycles, register)
            cycles += 1
            value = command.split()[1]
            register += int(value)


if __name__ == "__main__":
    part1()
    part2()
