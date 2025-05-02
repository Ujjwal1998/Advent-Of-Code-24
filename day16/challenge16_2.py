import heapq

with open("input.txt") as raw_input:
    grid = [list(line) for line in raw_input.read().split("\n")]
print(grid)
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == "S":
            sr = r
            sc = c
            break
    else:
        continue
pq = [(0, sr, sc, 0, 1, None, None, None, None)]
lowest_cost = {(sr, sc, 0, 1): 0}
backtrack = {}
best_cost = float("inf")
# why we need visited ? TO AVOID LOOOOOPS
while pq:
    cost, cr, cc, dr, dc, lr, lc, ldr, ldc = heapq.heappop(pq)
    if cost > lowest_cost.get((cr, cc, dr, dc), float("inf")):
        continue
    lowest_cost[(cr, cc, dr, dc)] = cost
    if grid[cr][cc] == "E":
        if cost > best_cost:
            break
        best_cost = cost
    if (cr, cc, dr, dc) not in backtrack:
        backtrack[(cr, cc, dr, dc)] = set()
    backtrack[(cr, cc, dr, dc)].add((lr, lc, ldr, ldc))
    for next_cost, nr, nc, ndr, ndc in [
        (cost + 1, cr + dr, cc + dc, dr, dc),
        (cost + 1000, cr, cc, dc, -dr),
        (cost + 1000, cr, cc, -dc, dr),
    ]:
        # print(nr, nc)
        if nr < 0 or nr > len(grid) or nc < 0 or nc > len(grid[0]):
            continue
        if grid[nr][nc] == "#":
            continue
        if cost > lowest_cost.get((nr, nc, ndr, ndc), float("inf")):
            continue
        heapq.heappush(pq, (next_cost, nr, nc, ndr, ndc, r, c, dr, dc))

print(backtrack)
