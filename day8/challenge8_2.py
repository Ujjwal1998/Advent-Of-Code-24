import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))) + "/input.txt"
with open(__location__) as raw_input:
    INPUT = raw_input.read().strip().split("\n")
m = len(INPUT)
n = len(INPUT[0])
map = {}
ans = set()
def withinBounds(point):
    x,y = point
    if (0<=x<m) and (0<=y<n):
        return True
    return False
def add_antinode(point1, point2):
    x1,y1 = point1
    x2,y2 = point2
    slope_x = x2 - x1
    slope_y = y2 - y1
    i = 0
    while True:
        newpoint1 = (x1 - slope_x * i, y1 - slope_y * i)
        if withinBounds(newpoint1):
            ans.add(newpoint1)
        else:
            break
        i += 1
    i = 0
    while True:
        newpoint2 = (x2 + slope_x * i, y2 + slope_y * i)
        if withinBounds(newpoint2):
            ans.add(newpoint2)
        else:
            break
        i += 1
for row in range(0,m):
    for col in range(0,n):
        current = INPUT[row][col]
        if current != ".":
            if current not in map.keys():
                map[current] = [(row,col)]
            else:
                map[current].append((row,col))
for key,vals in map.items():
    for i in range(len(vals)):
        for j in range(i+1, len(vals)):
            # print(i,j)
            add_antinode(vals[i], vals[j])
print(len(ans), ans)