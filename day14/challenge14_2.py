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
min_sf = float("inf")
best_iteration = None


def move(robot):
    px = (robot["pos"][0] + robot["velo"][0] + M) % M
    py = (robot["pos"][1] + robot["velo"][1] + N) % N
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
    # print(q1, q2, q3, q4)
    res = q1 * q2 * q3 * q4
    return res


for second in range(M * N):
    result = []
    for idx, robot in enumerate(robots):
        move(robot)
    sf = safety_factor(robots)
    print(sf, second, idx)
    if sf < min_sf:
        min_sf = sf
        best_iteration = second
print(best_iteration)
# seen = {}
# step = 0


# def draw():
#     global seen, step
#     while True:
#         picture = [["-" for _ in range(N)] for _ in range(M)]
#         for robot in robots:
#             px, py = robot["pos"]
#             print(px, py)
#             print(picture[px][py], "yo")
#             picture[px][py] = "&"
#             print(len(picture), len(picture[0]))
#         picture = "\n".join(["".join(line) for line in picture])
#         if picture in seen:
#             print(f"Saw this picture at step {seen[picture]}, stopping...")
#             print("here")
#             # return
#             break
#         seen[picture] = step
#         print(picture)
#         print("\n" * 2)
#         # for robot in robots:
#         move(robot)
#         step += 1
#         # print("=" * 90)
#         # print(robots)


# print(safety_factor(robots))
# draw()
# print(seen)
# with open("output.txt", "w") as raw_output:
#     for key in seen.keys():
#         raw_output.write(key)
