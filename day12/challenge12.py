import os
from collections import deque

__location__ = (
    os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    + "/input.txt"
)
with open(__location__) as raw_input:
    grid = [list(line) for line in raw_input.read().strip().split("\n")]

print(grid)
n = len(grid)
print(n)

dd = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited = set()


def bfs(i, j):
    dq = deque([(i, j)])
    region = set()
    region.add((i, j))
    visited.add((i, j))
    area = 0
    perimeter = 0
    while len(dq) > 0:
        ni, nj = dq.popleft()
        area += 1
        for di, dj in dd:
            ii, jj = ni + di, nj + dj
            if ii < n and ii >= 0 and jj < n and jj >= 0:
                if (ii, jj) not in region:
                    if grid[ni][nj] == grid[ii][jj]:
                        visited.add((ii, jj))
                        region.add((ii, jj))
                        dq.append((ii, jj))
                    else:
                        perimeter += 1
            else:
                perimeter += 1
    print(area, perimeter)
    return area, perimeter


def perimeter(region):
    ans = 0
    for i, j in region:
        ans += 4
        for di, dj in dd:
            ii, jj = i + di, j + dj
            if (ii, jj) in region:
                ans -= 1
    return ans


regions = []
res2 = 0
for i in range(n):
    for j in range(n):
        if (i, j) not in visited:
            # regions.append(bfs(i, j))
            a, p = bfs(i, j)
            res2 += a * p

print(res2)
# def cost(region):
#     p = perimeter(region)
#     a = len(region)
#     return p * a


# res = 0
# for r in regions:
#     res += cost(r)
# print(regions, res)
# print(len(bfs(0, 0, grid[0][0])), "AREA", grid[0][0], "NODE")
