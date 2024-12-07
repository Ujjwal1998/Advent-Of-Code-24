import os
from collections import deque
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))) + "\input.txt"
grid = []
with open(__location__) as raw_input:
    for line in raw_input.read().strip().split("\n"):
        row = []
        for char in line:
            row.append(char)
        grid.append(row)
m = len(grid)
n = len(grid[0])
DIRECTIONS = {"^":(-1,0),">":(0,1),"v":(1,0), "<":(0,-1)}
NEXT_DIRECTIONS = {'^': '>','>': 'v','v': '<','<': '^'}
START_POSITION = None
CURRENT_SYMBOL = "^"
for i in range((m)):
    for j in range((n)):
        if grid[i][j] == "^":
            START_POSITION = (i,j)
            break
seen = set()
while True:
    seen.add(START_POSITION)
    curr_x, curr_y = START_POSITION
    next_x, next_y = curr_x + DIRECTIONS[CURRENT_SYMBOL][0], curr_y + DIRECTIONS[CURRENT_SYMBOL][1]
    if not (0 <= next_x < n and 0 <= next_y < n):
        break
    if grid[next_x][next_y] == "#":
        CURRENT_SYMBOL = NEXT_DIRECTIONS[CURRENT_SYMBOL]
        continue
    START_POSITION = (next_x,next_y)
# ans1 -> len(seen)
def will_loop(x,y):
    if grid[x][y] == "#":
        return False
    grid[x][y] = "#"
    CURRENT_SYMBOL = "^"
    CURRENT_POSITION = START_POSITION
    new_seen = set()
    while True:
        if (CURRENT_POSITION[0],CURRENT_POSITION[1],CURRENT_SYMBOL) in new_seen:
            grid[x][y] = "."
            return True
        new_seen.add((CURRENT_POSITION[0],CURRENT_POSITION[1],CURRENT_SYMBOL))
        curr_x, curr_y = CURRENT_POSITION
        next_x, next_y = curr_x + DIRECTIONS[CURRENT_SYMBOL][0], curr_y + DIRECTIONS[CURRENT_SYMBOL][1]
        if not (0 <= next_x < n and 0 <= next_y < n):
            grid[x][y] = "."
            return False
        if grid[next_x][next_y] == "#":
            CURRENT_SYMBOL = NEXT_DIRECTIONS[CURRENT_SYMBOL]
        else:
            CURRENT_POSITION = (next_x,next_y)

res= 0
for oi, oj in seen:
    if oi == START_POSITION[0] and oj == START_POSITION[1]:
        continue
    loop = will_loop(oi, oj)
    res += loop
# ans2-> res