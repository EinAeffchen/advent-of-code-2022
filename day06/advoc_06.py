from pathlib import Path
from typing import Generator


def read_input() -> map:
    with open(Path(__file__).parent / "input", "r") as i:
        return i.read()


def get_marker_position(msg: str, n: int):
    for i in range(len(msg)):
        if len(set(msg[i : i + 14])) == 14:
            return i + 14


if __name__ == "__main__":
    message = read_input()
    print(get_marker_position(message, 4))  # part1
    print(get_marker_position(message, 14))  # part2
