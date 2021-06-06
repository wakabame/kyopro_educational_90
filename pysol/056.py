N, S = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]
DP = [[False for _ in range(S+1)] for _ in range(N+1)]
# DP[n][s] ... n 個まで選んだ時に重量sを達成できるか
DP[0][0] = True
for n in range(N):
    a, b = AB[n]
    for s in range(1,S+1):
        curr = False
        if s - a >= 0:
            curr |= DP[n][s-a]
        if s - b >= 0:
            curr |= DP[n][s-b]
        DP[n+1][s] = curr

w = S
if DP[-1][-1]:
    ans = [""]
    for n in range(N)[::-1]:
        a, b = AB[n]
        if w - a >= 0 and DP[n][w-a]:
            ans += ["A"]
            w -= a
        else:
            ans += ["B"]
            w -= b
    print("".join(ans[::-1]))
else:
    print("Impossible")
