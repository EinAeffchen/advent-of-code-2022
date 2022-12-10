from __future__ import annotations
from pathlib import Path


def read_input() -> map:
    with open(Path(__file__).parent / "input", "r") as i:
        return list(map(lambda x: x.split(), i.readlines()))


def follow(h_pos: list, t_pos: list, direction: str):
    move_x = h_pos[0] - t_pos[0]
    move_y = h_pos[1] - t_pos[1]
    if abs(move_x) > 1 or abs(move_y) > 1:
        if move_x == 0:
            t_pos[1] += move_y // 2
        elif move_y == 0:
            t_pos[0] += move_x // 2
        else:
            t_pos[0] += 1 if move_x > 0 else -1
            t_pos[1] += 1 if move_y > 0 else -1


def calc_t(direction: str, h_pos: list):
    if direction == "U":
        h_pos[1] += 1
    elif direction == "D":
        h_pos[1] -= 1
    elif direction == "R":
        h_pos[0] += 1
    elif direction == "L":
        h_pos[0] -= 1


t_positions = set()

if __name__ == "__main__":
    data = read_input()
    rope_length = 10  # part 2
    rope = [[0, 0] for _ in range(rope_length)]
    # part 2 still broken
    for movement in data:
        direction = movement[0]
        distance = int(movement[1])
        for _ in range(distance):
            calc_t(direction, rope[0])
            for i in range(rope_length - 1):
                follow(rope[i], rope[i + 1], direction)
                if i == rope_length - 2:
                    t_positions.add(tuple(rope[i + 1]))
        print(rope)
    print(len(t_positions))
