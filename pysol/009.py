from math import atan2, pi

N = int(input())

XY = []
for _ in range(N):
    XY += [list(map(int, input().split()))]

ans = 0
# 中点をfixして、x軸とのなす角で偏角ソート
for i in range(N):
    x0, y0 = XY[i]
    thetas = []
    for j in range(N):
        if i == j:
            continue
        x1, y1 = XY[j]
        theta = atan2(y1 - y0, x1 - x0) * 180 / pi
        thetas += [theta]
    thetas.sort()
    for j in range(N - 1):
        thetas += [thetas[j] + 360]
    i, j = 0, 0
    curr = 0
    while thetas[i] < 180:
        theta_diff = thetas[j] - thetas[i]
        curr = max(curr, 180 - abs(180 - theta_diff))
        if theta_diff > 180:
            i += 1
        else:
            j += 1
    ans = max(curr, ans)


print(ans)
