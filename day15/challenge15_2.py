from copy import deepcopy

with open("input.txt") as raw_input:
    top, bot = raw_input.read().split("\n\n")
    # grid = [list(line) for line in parts[0].split("\n")]
    # moves = parts[1].replace("\n", "")
expansion = {"#": "##", "O": "[]", ".": "..", "@": "@."}


def pretty(picure):
    for pic in picure:
        print(pic)


# def build_double_grid():
#     global grid
#     double_grid = []
#     for i in range(len(grid)):
#         row = []
#         for j in range(len(grid)):
#             if grid[i][j] == "@":
#                 row.append("@")
#                 row.append(".")
#             elif grid[i][j] == "#":
#                 row.append("#")
#                 row.append("#")
#             elif grid[i][j] == "O":
#                 row.append("[")
#                 row.append("]")
#             else:
#                 row.append(".")
#                 row.append(".")
#         double_grid.append(row)
#     return double_grid


# grid = build_double_grid()
grid = [list("".join(expansion[char] for char in line)) for line in top.splitlines()]
moves = bot.replace("\n", "")
M = len(grid)
N = len(grid[0])
mapping = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}


def within_bounds(x, y):
    global M, N
    return x >= 0 and x < M and y >= 0 and y < N


for i in range(M):
    for j in range(N):
        if grid[i][j] == "@":
            break
    else:
        continue
    break
print(i, j)
for m in moves:
    print(m)
    pretty(grid)

    targets = [(i, j)]
    # print(targets)
    # di = mapping[m][0]
    # dj = mapping[m][1]
    di = {"^": -1, "v": 1}.get(m, 0)
    dj = {"<": -1, ">": 1}.get(m, 0)
    go = True
    for ci, cj in targets:
        ni, nj = ci + di, cj + dj
        if (ni, nj) in targets:
            continue
        char = grid[ni][nj]
        if char == "#":
            go = False
            break
        if char == "[":
            targets.append((ni, nj))
            targets.append((ni, nj + 1))
        if char == "]":
            targets.append((ni, nj))
            targets.append((ni, nj - 1))
    if not go:
        continue
    copy = deepcopy(grid)
    grid[i][j] = "."
    grid[i + di][j + dj] = "@"
    # print(targets)
    # print("2")
    # pretty(grid)
    for bi, bj in targets[1:]:
        grid[bi][bj] = "."
    # print("3")
    # pretty(grid)
    for bi, bj in targets[1:]:
        # print(grid[bi + di][bj + dj], copy[bi][bj])
        grid[bi + di][bj + dj] = copy[bi][bj]
    # print("final")
    pretty(grid)
    i += di
    j += dj

    pretty(grid)
res = 0
for row in range(M):
    for col in range(N):
        if grid[row][col] == "[":
            res += row * 100 + col
print(res)
