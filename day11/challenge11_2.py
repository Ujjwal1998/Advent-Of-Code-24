import os
from collections import deque
from functools import cache

__location__ = (
    os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    + "/input.txt"
)

with open(__location__) as raw_input:
    INPUT = raw_input.read().strip().split(" ")


@cache
def check(stone, steps):
    if steps == 0:
        return 1
    if stone == 0:
        return check(1, steps - 1)
    string = str(stone)
    length = len(string)
    if length % 2 == 0:
        left = string[: length // 2]
        right = (
            0
            if len(string[length // 2 :].lstrip("0")) == 0
            else string[length // 2 :].lstrip("0")
        )
        return check(int(left), steps - 1) + check(int(right), steps - 1)
    return check(stone * 2024, steps - 1)
