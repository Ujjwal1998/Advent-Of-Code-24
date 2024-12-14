import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))) + "\input.txt"
with open(__location__) as raw_input:
    SCENARIOS = raw_input.read().split("\n\n")
res = 0
def solve(ax,ay,bx,by,px,py):
    i = (by * px - bx * py) // (by * ax - bx * ay)
    j = (px - ax * i) // bx
    # j = (px*ay-py*ax)//(ay*bx-by*ax)
    print(i, j, px)
    if ax * i + bx * j == px and ay * i + by * j == py:
        return (3 * i) + j
    return 0
for scenario in SCENARIOS:
    a,b,prize = scenario.split("\n")
    ax,ay,bx,by,px,py = a.split(":")[1].split(",")[0].split("+")[1],a.split(":")[1].split(",")[1].split("+")[1], b.split(":")[1].split(",")[0].split("+")[1],b.split(":")[1].split(",")[1].split("+")[1], prize.split(":")[1].split(",")[0].split("=")[1], prize.split(":")[1].split(",")[1].split("=")[1]
    res += solve(int(ax),int(ay),int(bx),int(by),int(px) + 10000000000000,int(py) + 10000000000000)
print(res)
# 75189228471714.0
74914228471331
