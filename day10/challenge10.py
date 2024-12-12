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


def get_neighbors(root):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
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


def bfs_and_count_zero(root):
    count = 0
    queue = deque([root])
    visited = set()
    while len(queue) > 0:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        x, y = node
        if INPUT[x][y] == 9:
            count += 1
        else:
            for nei in get_neighbors(node):
                if nei not in visited:
                    queue.append(nei)
    return count


for i in range(0, m):
    for j in range(0, n):
        if INPUT[i][j] == 0:
            # traverse and then find if it reaches 9, if it reaches 9 count how many 9s it can reach and keep incrementing the res
            res += bfs_and_count_zero((i, j))
print(res)
