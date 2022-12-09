from __future__ import annotations
from pathlib import Path


def read_input() -> map:
    with open(Path(__file__).parent / "input", "r") as i:
        return list(map(lambda x: x.split(), i.readlines()))


def calc_t(movement: list[str, int], rope: list, i: int):
    direction = movement[0]
    distance = int(movement[1])

    h_pos = rope[i]
    t_pos = rope[i + 1]

    for _ in range(distance):
        if direction == "U":
            h_pos[1] += 1
            if abs(t_pos[1] - h_pos[1]) > 1:
                t_pos[1] += 1
                if diff := h_pos[0] - t_pos[0]:
                    t_pos[0] += diff
        elif direction == "D":
            h_pos[1] -= 1
            if abs(t_pos[1] - h_pos[1]) > 1:
                t_pos[1] -= 1
                if diff := h_pos[0] - t_pos[0]:
                    t_pos[0] += diff
        elif direction == "R":
            h_pos[0] += 1
            if abs(t_pos[0] - h_pos[0]) > 1:
                t_pos[0] += 1
                if diff := h_pos[1] - t_pos[1]:
                    t_pos[1] += diff
        elif direction == "L":
            h_pos[0] -= 1
            if abs(t_pos[0] - h_pos[0]) > 1:
                t_pos[0] -= 1
                if diff := h_pos[1] - t_pos[1]:
                    t_pos[1] += diff
        # print(t_pos)
        if i == 8:
            t_positions.add(tuple(t_pos))


t_positions = set()

if __name__ == "__main__":
    data = read_input()
    rope = [[0, 0] for _ in range(10)]
    # part 2 still broken
    for movement in data:
        for i, knot in enumerate(rope[:-1]):
            calc_t(movement, rope, i)
    print(len(t_positions))
