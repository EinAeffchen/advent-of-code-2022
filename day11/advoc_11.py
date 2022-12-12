from __future__ import annotations
from pathlib import Path
from math import floor
from typing import List, Dict
from operator import add, mul
from math import pow
from numpy import array_split
import re


def get_stress_calculation(text: str) -> tuple:
    stress_function_descriptor = text.replace("Operation: new = ", "")
    if "*" in stress_function_descriptor:
        stress_level_function = mul
        if "* old" not in stress_function_descriptor:
            operator = "*"
        else:
            operator = "*"
            stress_level_function = pow
    else:
        stress_level_function = add
        operator = "+"
    stress_level_function_value: str = stress_function_descriptor.replace(
        f"old {operator}", ""
    ).strip()
    if stress_level_function_value.isnumeric():
        stress_level_function_value = int(stress_level_function_value)
    return stress_level_function, stress_level_function_value


def parse_input(text: list) -> dict:
    data = dict()
    data["id"] = int(re.match("Monkey (\d):", text[0].strip()).group(1))
    data["items"] = [
        int(item)
        for item in text[1].strip().replace("Starting items:", "").split(",")
    ]
    (
        data["stress_level_function"],
        data["stress_level_value"],
    ) = get_stress_calculation(text[2].strip())
    data["action_condition"] = int(
        text[3].strip().replace("Test: divisible by ", "")
    )
    targets = [int(text[4].strip().replace("If true: throw to monkey", ""))]
    targets.append(
        int(text[5].strip().replace("If false: throw to monkey", ""))
    )
    data["targets"] = targets
    return data


def read_input() -> dict:
    with open(Path(__file__).parent / "input", "r") as i:
        guide = i.readlines()
        monkeys = [
            Monkey(**parse_input(text)) for text in array_split(guide, 8)
        ]
        return {monkey.id: monkey for monkey in monkeys}


class Item(object):
    worry_level: int

    def __init__(self, worry_level: int):
        self.worry_level = worry_level

    def relieve(self, level: int = 3):
        self.worry_level = floor(self.worry_level / level)

    def stress(self, level: int, function):
        if function == pow:
            self.worry_level = 2
        self.worry_level = function(level, self.worry_level)


class Monkey(object):
    id: int
    items: List[Item]
    action_condition: int
    stress_level_function: int
    stress_level_value: int
    targets: List[int]
    items_inspected: int

    def __init__(
        self,
        id: int,
        items: List[int],
        action_condition: int,
        stress_level_function,
        stress_level_value: int,
        targets: list,
    ):
        self.id = id
        self.items = [Item(item) for item in items]
        self.action_condition = action_condition
        self.stress_level_value = stress_level_value
        self.stress_level_function = stress_level_function
        self.targets = targets
        self.items_inspected = 0

    def inspect(self, comrades: Dict[int, Monkey]):
        while self.items:
            item = self.items.pop(0)
            self.items_inspected += 1
            if self.stress_level_value == "old":
                stress_value = item.worry_level
            else:
                stress_value = int(self.stress_level_value)
            item.stress(stress_value, self.stress_level_function)
            # item.relieve()
            self.throw_item(item, comrades)

    def receive_item(self, item: Item):
        self.items.append(item)

    def throw_item(self, item, comrades: Dict[int, Monkey]):
        if item.worry_level % self.action_condition == 0:
            comrades[self.targets[0]].receive_item(item)
        else:
            comrades[self.targets[1]].receive_item(item)


def part1(monkeys: Dict[int, Monkey]):
    for _ in range(20):
        monkey: Monkey
        for id, monkey in monkeys.items():
            monkey.inspect(monkeys)
    acitivity = [monkeys[monkey].items_inspected for monkey in monkeys]
    acitivity = sorted(acitivity, reverse=True)
    print(acitivity[0] * acitivity[1])


def part2(monkeys: Dict[int, Monkey]):
    for _ in range(10000):
        monkey: Monkey
        for id, monkey in monkeys.items():
            monkey.inspect(monkeys)
    acitivity = [monkeys[monkey].items_inspected for monkey in monkeys]
    acitivity = sorted(acitivity, reverse=True)
    print(acitivity[0] * acitivity[1])


if __name__ == "__main__":
    monkeys = read_input()
    part2(monkeys)
