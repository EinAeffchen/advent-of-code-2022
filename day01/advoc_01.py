from pathlib import Path
from typing import Generator

def read_input() -> Generator[int, None, None]:
    with open(Path(__file__).parent/"input", "r") as i:
        return map(lambda x: sum(map(int, x.strip().split("\n"))), i.read().split("\n\n"))
         
def get_highest_calories(data: Generator[int, None, None]):
    return max(data)

def get_sum_calories_for_top_n(data: Generator[int, None, None], n: int):
    return sum(sorted(data)[-n:])

if __name__ == '__main__':
    print(get_highest_calories(read_input()))
    print(get_sum_calories_for_top_n(read_input(), 3))