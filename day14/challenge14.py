import os

__location__ = (
    os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    + "/input.txt"
)
robots = []
with open(__location__) as raw_input:
    for line in raw_input.read().split("\n"):
        robot = {}
        pos, velo = line.split(" ")
        px, py = pos.split("=")[1].split(",")
        vx, vy = velo.split("=")[1].split(",")
        robot["pos"] = (int(px), int(py))
        robot["velo"] = (int(vx), int(vy))
        robots.append(robot)

M = 101
N = 103


def move(robot):
    px = (robot["pos"][0] + robot["velo"][0] + M) % M
    py = (robot["pos"][1] + robot["velo"][1] + N) % N
    # px = robot["pos"][0] + robot["velo"][0]
    # py = robot["pos"][1] + robot["velo"][1]
    # if px > M:
    #     px = px % M
    # elif px < 0:
    #     px = M - px
    # if py > N:
    #     py = py % N
    # elif py < 0:
    #     py = N - py
    robot["pos"] = (px, py)


def count_robots(x1, x2, y1, y2, px, py):
    ans = 0
    for i in range(x1, x2):
        for j in range(y1, y2):
            if px == i and py == j:
                ans += 1
    return ans


def safety_factor(robots):
    mid_hor = M // 2
    mid_vert = N // 2
    res = 1
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    for robot in robots:
        px, py = robot["pos"]
        q1 += count_robots(0, mid_hor, 0, mid_vert, px, py)
        q2 += count_robots(mid_hor + 1, M, 0, mid_vert, px, py)
        q3 += count_robots(0, mid_hor, mid_vert + 1, N, px, py)
        q4 += count_robots(mid_hor + 1, M, mid_vert + 1, N, px, py)
    print(q1, q2, q3, q4)
    res = q1 * q2 * q3 * q4
    return res


for i in range(100):
    for robot in robots:
        move(robot)
    # print("=" * 90)
    # print(robots)
print(safety_factor(robots))
