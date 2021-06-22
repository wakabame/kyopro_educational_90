H, W = map(int, input().split())
C = [input() for _ in range(H)]

dh = [1, -1, 0, 0]
dw = [0, 0, 1, -1]


def dfs(h, w, st, en, route):
    if h < 0 or h >= H or w < 0 or w >= W:
        return -1
    if C[h][w] == "#":
        return -1

    if (h, w) in route:
        if route[0] == (h, w):
            return len(route)
        else:
            return -1

    ret = -1
    for i in range(4):
        h_ = h + dh[i]
        w_ = w + dw[i]
        ret = max(ret, dfs(h_, w_, st, en, route+ [(h, w)]))

    return ret

ans = -1
for h in range(H):
    for w in range(W):
        ans = max(ans, dfs(h, w, h, w, []))

if ans == 2:
    print(-1)
else:
    print(ans)
