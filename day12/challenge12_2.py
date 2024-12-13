import os
from collections import deque

__location__ = (
    os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    + "/input.txt"
)
with open(__location__) as raw_input:
    grid = [list(line) for line in raw_input.read().strip().split("\n")]

# print(grid)
n = len(grid)
# print(n)

dd = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited = set()


def bfs(i, j):
    dq = deque([(i, j)])
    region = set()
    region.add((i, j))
    visited.add((i, j))
    while len(dq) > 0:
        ni, nj = dq.popleft()
        for di, dj in dd:
            ii, jj = ni + di, nj + dj
            if ii < n and ii >= 0 and jj < n and jj >= 0:
                if (ii, jj) not in region and grid[ni][nj] == grid[ii][jj]:
                    visited.add((ii, jj))
                    region.add((ii, jj))
                    dq.append((ii, jj))
    return region


def sides(region):
    corner_candidates = set()
    for i, j in region:
        for ci, cj in [
            (i - 0.5, j - 0.5),
            (i + 0.5, j - 0.5),
            (i + 0.5, j + 0.5),
            (i - 0.5, j + 0.5),
        ]:
            corner_candidates.add((ci, cj))
    print(corner_candidates)
    corners = 0
    for ci, cj in corner_candidates:
        config = [
            (si, sj) in region
            for si, sj in [
                (ci - 0.5, cj - 0.5),
                (ci + 0.5, cj - 0.5),
                (ci + 0.5, cj + 0.5),
                (ci - 0.5, cj + 0.5),
            ]
        ]
        number = sum(config)
        if number == 1:
            corners += 1
        elif number == 2:
            if config == [True, False, True, False] or config == [
                False,
                True,
                False,
                True,
            ]:
                corners += 2
        elif number == 3:
            corners += 1
    return corners


regions = []
for i in range(n):
    for j in range(n):
        if (i, j) not in visited:
            regions.append(bfs(i, j))


def cost(region):
    s = sides(region)
    a = len(region)
    return s * a


res = 0
for r in regions:
    res += cost(r)
# print(regions, res)
# print(len(bfs(0, 0, grid[0][0])), "AREA", grid[0][0], "NODE")
