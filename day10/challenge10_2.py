import os
from collections import deque

__location__ = (
    os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    + "/input.txt"
)
INPUT = []
with open(__location__) as raw_input:
    for line in raw_input.read().strip().split("\n"):
        INPUT.append([int(digit) for digit in line])
m = len(INPUT)
n = len(INPUT[0])
res = 0


directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def get_neighbors(root):
    neighbors = []
    x, y = root
    for dx, dy in directions:
        nei_x, nei_y = x + dx, y + dy
        if (
            nei_x >= 0
            and nei_x < m
            and nei_y >= 0
            and nei_y < n
            and INPUT[nei_x][nei_y] - INPUT[root[0]][root[1]] == 1
        ):
            neighbors.append((nei_x, nei_y))
    return neighbors


def recur(root):
    x, y = root
    if INPUT[x][y] == 9:
        return 1
    rating = 0
    for dx, dy in directions:
        xx, yy = x + dx, y + dy
        if xx >= 0 and xx < m and yy >= 0 and yy < n:
            if INPUT[xx][yy] - INPUT[x][y] == 1:
                rating += recur((xx, yy))
    return rating


for i in range(0, m):
    for j in range(0, n):
        if INPUT[i][j] == 0:
            res += recur((i, j))
print(res)
