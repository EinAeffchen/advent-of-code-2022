from pathlib import Path
from operator import add
from functools import reduce


def read_input() -> map:
    with open(Path(__file__).parent / "input", "r") as i:
        return map(
            lambda x: [y.split("-") for y in x.strip().split(",")], i.readlines()
        )


def range_to_set(sections: list) -> set:
    return set(range(int(sections[0]), int(sections[1]) + 1))


def contains_the_other(sections: list) -> int:
    set1 = range_to_set(sections[0])
    set2 = range_to_set(sections[1])
    return set1.issubset(set2) or set2.issubset(set1)


def overlaps_the_other(ranges: list):
    set1 = range_to_set(ranges[0])
    set2 = range_to_set(ranges[1])
    return bool(set1 & set2)


if __name__ == "__main__":
    print(reduce(add, map(contains_the_other, read_input()), 0))  # part1
    print(reduce(add, map(overlaps_the_other, read_input()), 0))  # part2
