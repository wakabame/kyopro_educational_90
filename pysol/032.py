from itertools import permutations

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
dislike = [[] for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    dislike[x - 1] += [y - 1]
    dislike[y - 1] += [x - 1]

ans = float("INF")
for perm in permutations(range(N)):
    curr = 0
    last_runner = -1
    for i, v in enumerate(perm):
        # 第i区はvさんが走る
        curr += A[v][i]
        if last_runner >= 0:
            if v in dislike[last_runner] or last_runner in dislike[v]:
                break
        last_runner = v
    else:
        ans = min(curr, ans)

if ans == float("INF"):
    print(-1)
else:
    print(ans)
