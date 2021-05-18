from collections import deque
H, W = map(int, input().split())
rs, cs = map(int, input().split())
rt, ct = map(int, input().split())
C = [input() for _ in range(H)]


def check_movable(h, w):
    if h < 0 or h >= H or w < 0 or w >= W:
        return False
    elif C[h][w] == "#":
        return False
    else:
        return True

# それぞれのマスまでの最短距離
distance = [[float("INF") for _ in range(W)] for w_ in range(H)]

# 0-1 BFS
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# d は (向き, [今のマスの座標], 今のコスト) を要素に持つ
d = deque([(None, [rs-1, cs-1], 0)])
while d:
    direct, [h, w], cost = d.pop()
    if cost > distance[h][w]:
        # cost がすでに到達してきた距離より進に大きい場合はskip
        # 同着は向きがあるので入れる
        continue
    distance[h][w] = min(distance[h][w], cost)
    for i, [dh, dw] in enumerate(zip(dx, dy)):
        # 上下左右の4方向について1マスずつ進む
        # 同じ向きならば同コストで追加（幅優先の性質からコストチェック不要）
        # 異なる向きについては, cost+1 以下ならば末尾に追加する
        h_ = h+dh
        w_ = w+dw
        if not check_movable(h_, w_):
            continue
        if direct == i:
            d.append((i, [h_, w_], cost))
        else:
            if cost <= distance[h_][w_] + 1:
                d.appendleft((i, [h_, w_], cost+1))

print(distance[rt-1][ct-1]-1)
