from __future__ import annotations
from pathlib import Path
from functools import reduce
from typing import List
from operator import mul


def read_input() -> map:
    with open(Path(__file__).parent / "input", "r") as i:
        lines = list(map(lambda x: x.strip(), i.readlines()))
    forest = list()
    for x, line in enumerate(lines):
        forest.append(list())
        for y, tree in enumerate(line):
            forest[x].append(make_tree(tree, x=x, y=y, forest=lines))
    return forest


def set_row(forest: List[str], x: int, y: int, type: str) -> list:
    if type == "up":
        row = [forest[x - i][y] for i in range(1, x + 1)]
    elif type == "down":
        row = [forest[x + i][y] for i in range(1, len(forest) - x)]
    elif type == "left":
        row = list(reversed(forest[x][:y]))
    elif type == "right":
        row = forest[x][y + 1 :]
    return list(map(int, row))


def make_tree(height: str, **kwargs):
    up = set_row(type="up", **kwargs)
    down = set_row(type="down", **kwargs)
    left = set_row(type="left", **kwargs)
    right = set_row(type="right", **kwargs)
    tree = Tree(int(height), up, right, down, left)
    return tree


class Tree:
    height: int
    up: list
    down: list
    right: list
    left: list

    def __init__(self, height: int, up, right, down, left):
        self.height = height
        self.up = up
        self.right = right
        self.left = left
        self.down = down
        self.directions: List[int] = [self.up, self.down, self.right, self.left]

    def scenic_score(self) -> int:
        viewing_lengths = list()
        for direction in self.directions:
            if not direction:
                viewing_lengths.append(0)
                continue
            try:
                viewing_length = len(
                    direction[
                        : next(
                            i
                            for i in range(len(direction))
                            if direction[i] >= self.height
                        )
                        + 1
                    ]
                )
            except StopIteration:
                viewing_length = len(direction)
            if viewing_length:
                viewing_lengths.append(viewing_length)
        if viewing_lengths:
            return reduce(mul, viewing_lengths)
        else:
            return 0

    def is_visible(self):
        return not all(self.directions) or any(
            [
                all([self.height > tree for tree in direction])
                for direction in self.directions
            ]
        )


if __name__ == "__main__":
    forest = read_input()
    print(sum([tree.is_visible() for row in forest for tree in row]))
    print(max([tree.scenic_score() for row in forest for tree in row]))
