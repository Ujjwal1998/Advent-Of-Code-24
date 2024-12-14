import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))) + "\input.txt"
with open(__location__) as raw_input:
    SCENARIOS = raw_input.read().split("\n\n")
res = 0
def solve(ax,ay,bx,by,px,py):
    candidates = []
    for i in range(100):
        for j in range(100):
            if (i * ax + j * bx == px) and (i * ay + j * by == py):
                candidates.append(3*i + j)
    if candidates:
        print(candidates)
        return min(candidates)
    return 0
for scenario in SCENARIOS:
    a,b,prize = scenario.split("\n")
    ax,ay,bx,by,px,py = a.split(":")[1].split(",")[0].split("+")[1],a.split(":")[1].split(",")[1].split("+")[1], b.split(":")[1].split(",")[0].split("+")[1],b.split(":")[1].split(",")[1].split("+")[1], prize.split(":")[1].split(",")[0].split("=")[1], prize.split(":")[1].split(",")[1].split("=")[1]
    res += solve(int(ax),int(ay),int(bx),int(by),int(px),int(py))
print(res)
