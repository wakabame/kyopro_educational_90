N = int(input())
S = input()
s = "atcoder"
DP = [[0 for _ in range(N + 1)] for _ in range(8)]
for i in range(N + 1):
    DP[0][i] = 1

for i in range(7):
    for k in range(N):
        DP[i + 1][k + 1] = DP[i + 1][k]
        if S[k] == s[i]:
            DP[i + 1][k + 1] = (DP[i + 1][k + 1] + DP[i][k]) % (10 ** 9 + 7)

print(DP[-1][-1])
