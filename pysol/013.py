"""
AGC 王国には N 個の交差点があり、それぞれ 1, 2, 3, ..., N と番号付けられています。
また M 本の道路があり、道路 i は交差点 A[i] と交差点 B[i] を双方向に結び、交差点間の移動にかかる時間は C[i] 秒です。

今日から数えて i (1≦i≦N) 日目には交差点 i でイベントが開催されるため、移動の際には交差点 i を経由しなければなりません、
i = 1, 2, 3, ..., N それぞれについて、i 日目に交差点 1 から交差点 N まで移動するのにかかる時間の最小値を求めてください。

【制約】
・2 ≦ N ≦ 100000　←　こっちが正しいです！
・1 ≦ M ≦ 100000
・1 ≦ A[i] < B[i] ≦ N
・(A[i], B[i]) ≠ (A[j], B[j]) [i ≠ j]
・1 ≦ C[i] ≦ 10000
・いくつかの道路を通って、都市 1 から都市 N までたどり着ける
・入力はすべて整数

"""
# 各 i について、「頂点1から頂点iまでの距離」+「頂点iから頂点Nまでの距離」を算出
# 任意の二点間の距離を求めるワーシャルフロイドだとO(N^3)なので間に合わない
# ダイクストラで「頂点1から頂点iまでの距離」を計算しておく
# ダイクストラで「頂点iから頂点Nまでの距離」をを計算しておく

from heapq import heappush, heappop
N, M = map(int, input().split())

adj = [[] for i in range(N)] # 始点を i とするedgeの集合
for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a-1] += [(b-1, c)]
    adj[b-1] += [(a-1, c)]
     
distance_from_start = [float("inf") for i in range(N)] # 頂点 i までの最短距離
distance_from_start[0] = 0
distance_from_destination = [float("inf") for i in range(N)] # 頂点 i までの最短距離
distance_from_destination[N-1] = 0
     
confirm = [False] * N # 頂点までの距離が確定しているか
# hq は [頂点kまでの最短距離, 頂点k] を要素に持つ
# ヒープキューのソートキーにするため、最短距離が第一変数
hq = [(0, 0)]
# ダイクストラ法
while hq:
    d, v = heappop(hq)
    if confirm[v]:
        continue
    confirm[v] = True
    for w, c in adj[v]:
        if not confirm[w] and d + c < distance_from_start[w]:
            distance_from_start[w] = d + c
            heappush(hq, (distance_from_start[w], w))

confirm = [False] * N # 頂点までの距離が確定しているか
hq = [(0, N-1)]
# ダイクストラ法
while hq:
    d, v = heappop(hq)
    if confirm[v]:
        continue
    confirm[v] = True
    for w, c in adj[v]:
        if not confirm[w] and d + c < distance_from_destination[w]:
            distance_from_destination[w] = d + c
            heappush(hq, (distance_from_destination[w], w))


for i in range(N):
    print(distance_from_start[i] + distance_from_destination[i])
