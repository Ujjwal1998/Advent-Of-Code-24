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
pq = [(0, sr, sc, 0, 1)]
visited = {(sr, sc, 0, 1)}
# why we need visited ? TO AVOID LOOOOOPS
while pq:
    cost, cr, cc, dr, dc = heapq.heappop(pq)
    if grid[cr][cc] == "E":
        print(cost)
        break
    visited.add((cr, cc, dr, dc))
    for next_cost, nr, nc, ndr, ndc in [
        (cost + 1, cr + dr, cc + dc, dr, dc),
        (cost + 1000, cr, cc, dc, -dr),
        (cost + 1000, cr, cc, -dc, dr),
    ]:
        print(nr, nc)
        if nr < 0 or nr > len(grid) or nc < 0 or nc > len(grid[0]):
            continue
        if grid[nr][nc] == "#":
            continue
        if (nr, nc, ndr, ndc) in visited:
            # cheaper way already found
            continue
        heapq.heappush(pq, (next_cost, nr, nc, ndr, ndc))
