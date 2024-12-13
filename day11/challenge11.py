import os
from functools import cache

__location__ = (
    os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    + "/input.txt"
)

with open(__location__) as raw_input:
    INPUT = raw_input.read().strip().split(" ")
print(INPUT)


def check(s):
    num = int(s)
    if num == 0:
        return " 1"
    if len(s) % 2 == 0:
        left = s[: len(s) // 2]
        right = (
            "0"
            if len(s[len(s) // 2 :].lstrip("0")) == 0
            else s[len(s) // 2 :].lstrip("0")
        )
        return " " + left + " " + right
    else:
        return " " + str(int(num * 2024))


@cache
def blink(str):
    res = ""
    for digit in str:
        res += check(digit)
    # print(res, type(res))
    return res.strip().split(" ")


@cache
def arrangement(no_of_blinks):
    res = blink(INPUT)
    for i in range(no_of_blinks - 1):
        res = blink(res)
        # print(res)
    return res


# once = blink(["125", "17"])
# print(once)
# twice = blink(once)
# print(twice)
# thrice = blink(twice)
# print(thrice)

print(len(arrangement(75)))
