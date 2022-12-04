from pathlib import Path
import string
from functools import reduce
from typing import List
from numpy import array_split


class Rucksack:
    def __init__(self, content: str):
        self.content = content.strip()
        self.first_compartement, self.second_compartement = (
            self.content[: len(self.content) // 2],
            self.content[len(self.content) // 2 :],
        )

    def get_common(self):
        return next(iter(set(self.first_compartement) & set(self.second_compartement)))


class Group:
    def __init__(self, rucksacks: List[str]):
        self.rucksacks = map(lambda x: set(Rucksack(x).content), rucksacks)

    def _check_joint_compartments(self, rucksack1: set, rucksack2: set):
        return rucksack1 & rucksack2

    def get_common(self):
        return next(iter(reduce(self._check_joint_compartments, self.rucksacks)))


def read_input() -> map:
    with open(Path(__file__).parent / "input", "r") as i:
        return i.readlines()


def part1(data: list):
    print(
        sum(
            map(lambda x: string.ascii_letters.find(Rucksack(x).get_common()) + 1, data)
        )
    )


def part2(data: list):
    groups = array_split(data, int(len(data) / 3))
    print(
        sum(
            map(
                lambda x: string.ascii_letters.find(Group(x).get_common()) + 1,
                groups,
            )
        )
    )


if __name__ == "__main__":
    part1(read_input())
    part2(read_input())
