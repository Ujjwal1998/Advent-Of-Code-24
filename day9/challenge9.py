import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))) + "/input.txt"
with open(__location__) as raw_input:
    INPUT = raw_input.read().strip().split("\n")[0]
n = len(INPUT)
def build_filesystem(diskmap):
    res = []
    counter = 0
    for i in range(n):
        current = int(diskmap[i])
        if (i % 2) != 0:
            for j in range(current):
                res.append(".")
        else:
            for j in range(current):
                res.append(counter)
            counter += 1
    return res
def move(arr):
    l = 0
    r = len(arr) - 1
    while l < r:
        while arr[l] != ".":
            l += 1
        while arr[r] == ".":
            r -= 1
        arr[l], arr[r] = arr[r], arr[l]
        r -= 1
        l += 1
    return arr
def checksum(arr):
    counter2 = 0
    ans = 0
    for i in range(len(arr)):
        if arr[i] != ".":
            # break
            ans += arr[i] * counter2
            counter2 += 1
    return ans

filesystem = build_filesystem(INPUT)
modified_filesystem = move(filesystem)
ans = checksum(modified_filesystem)
print("ANS",ans)