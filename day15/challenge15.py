with open("input.txt") as raw_input:
    parts = raw_input.read().split("\n\n")
    grid = [list(line) for line in parts[0].split("\n")]
    moves = parts[1].replace("\n", "")

n = len(grid)
print(moves)
# print(grid)
mapping = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}
for i in range(n):
    for j in range(n):
        # print(grid[i][j], i, j)
        if grid[i][j] == "@":
            p, q = i, j
            break

i, j = p, q


def within_bounds(x, y):
    return x >= 0 and x < n and y >= 0 and y < n


def pretty(picure):
    for pic in picure:
        print(pic)


for m in moves:
    # print(m)
    ii, jj = i + mapping[m][0], j + mapping[m][1]
    print(i, j, ii, jj, grid[ii][jj], m)
    # print(grid)
    if not within_bounds(ii, jj):
        continue
    if grid[ii][jj] == "#":
        continue
    elif grid[ii][jj] == ".":
        grid[ii][jj] = "@"
        grid[i][j] = "."
        i, j = ii, jj
    else:
        iii, jjj = ii, jj
        while within_bounds(iii, jjj):
            if grid[iii][jjj] == "#":
                break
            if grid[iii][jjj] == ".":
                fi, fj = iii, jjj
                grid[i][j] = "."
                grid[ii][jj] = "@"
                grid[fi][fj] = "O"
                i, j = ii, jj
                break
            iii += mapping[m][0]
            jjj += mapping[m][1]
res = 0
for row in range(n):
    for col in range(n):
        if grid[row][col] == "O":
            res += row * 100 + col
print(res)
