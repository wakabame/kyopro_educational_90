import sys

sys.setrecursionlimit(10 ** 5)

N = int(input())
edge = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    edge[a - 1] += [b - 1]
    edge[b - 1] += [a - 1]

dp = [0] * N


def dfs(u=None, v=0):
    dp[v] = 1
    for w in edge[v]:
        if w != u:
            dfs(v, w)
            dp[v] += dp[w]


def dfs2(u=None, v=0):
    ret = 0
    ret += dp[v] * (N - dp[v])
    for w in edge[v]:
        if w != u:
            ret += dfs2(v, w)
    return ret


dfs()
print(dfs2())
