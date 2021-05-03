N = int(input())

edges = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    edges[a - 1] += [b - 1]
    edges[b - 1] += [a - 1]

odd = []
even = [0]

st = [[0, 0]]
visited = [True] + [False] * (N - 1)

# DFS で0からの距離を計算する.
# 0 からの距離が偶数ならeven 奇数ならodd に拠点のindexを追加する
while st:
    u, d = st.pop()
    for v in edges[u]:
        if visited[v]:
            continue
        visited[v] = True
        if (d + 1) % 2:
            odd += [v]
        else:
            even += [v]
        st += [[v, d + 1]]

if len(even) >= N // 2:
    ans = even[: N // 2]
else:
    ans = odd[: N // 2]

print(*[v + 1 for v in ans])
