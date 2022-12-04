from pathlib import Path
from enum import Enum
from collections import namedtuple

class Opponent(Enum):
    A = 1 #rock
    B = 2 #paper
    C = 3 #scissors

class Self(Enum):
    X = 1
    Y = 2
    Z = 3

class Outcome(Enum):
    loss = 0
    draw = 3
    win = 6

class TargetOutcome(Enum):
    X = Outcome["loss"]
    Y = Outcome["draw"]
    Z = Outcome["win"]


def result_for_x_and_y(x:int, y:int):
    if x==y:
        return ("draw", "draw")
    elif x==3 and y==1:
        return ("loss", "win")
    elif x==1 and y==3:
        return ("win", "loss")
    elif x > y:
        return ("win", "loss")
    elif x < y:
        return ("loss", "win")

def get_points(hand1: str, hand2: str):
    opp = Opponent[hand1]
    pla = Self[hand2]
    _, player_result = result_for_x_and_y(opp.value, pla.value)
    return Outcome[player_result].value + pla.value

def read_input() -> map:
    with open(Path(__file__).parent/"input", "r") as i:
        return i.readlines()

def part1():
    print(sum(map(lambda x: get_points(*x.split()), read_input())))

def reverse_read(hand1: str, target_outcome: str):
    # yup I'm too lazy so I just bruteforce it...
    opp = Opponent[hand1]
    target_outcome_obj = TargetOutcome[target_outcome]
    for i in range(1,4):
        _, player_result = result_for_x_and_y(opp.value, i)
        if Outcome[player_result] == target_outcome_obj.value:
            return Outcome[player_result].value + i

def part2():
    print(sum(map(lambda x: reverse_read(*x.split()), read_input())))

if __name__ == '__main__':
    part1()
    part2()