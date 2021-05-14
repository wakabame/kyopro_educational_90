import sys

sys.setrecursionlimit(10 ** 5)

N = int(input())
edge = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    edge[a - 1] += [b - 1]
    edge[b - 1] += [a - 1]

count = [1] * N
ans = [0] * N


def dfs1(u=None, v=0):
    for w in edge[v]:
        if w != u:
            dfs1(v, w)
            count[v] += count[w]
            ans[v] += ans[w] + count[w]


def dfs2(u=None, v=0):
    for w in edge[v]:
        if w != u:
            ans[w] = ans[v] - count[w] + N - count[w]
            dfs2(v, w)


dfs1()
dfs2()
print(sum(ans) // 2)
