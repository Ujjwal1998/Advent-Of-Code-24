import os
from collections import defaultdict
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))) + "/input.txt"
with open(__location__) as raw_input:
    INPUT = raw_input.read().strip().split("\n")[0]
res = []
map = {}
pos = 0
spaces = []
fid = 0
res = []
for i in range(len(INPUT)):
    size = int(INPUT[i])
    if (i % 2) != 0:
        spaces.append([pos, size])
        res += (["."] * size)
    else:
        res += ([fid] * size)
        map[fid] = (fid,size)
        fid += 1
    pos += size
# print(map)
for key in map.keys():
    for idx, elem in enumerate(res):
        if elem == key:
            map[key] = (idx,map[key][1])
            break
# print(map,spaces)
n = len(res)
# print(res)
while fid > 0:
    fid -= 1 
    start_index, space_req = map[fid]
    for i, (space_index, space_size) in enumerate(spaces):
        # print(i, space_index, space_size)
        if space_index >= start_index:
            spaces = spaces[:i]
            break
        if space_req <= space_size:
            for j in range(0,space_req):
                res[start_index+j] = "."
            for k in range(0,space_req):
                res[space_index + k] = fid
            map[fid] = (space_index,space_req)
            if space_req == space_size:
                spaces.pop(i)
            else:
                spaces[i] = (space_index + space_req, space_size - space_req)
            break

# print(res)
def checksum(arr):
    ans = 0
    for i,x in enumerate(arr):
        if x != ".":
            ans += i * x
    return ans
print(checksum(res))
# 8607352322743 too high
# 6398065450842