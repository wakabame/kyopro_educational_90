N, B, K = map(int, input().split())
C = list(map(int, input().split()))
MOD = 10**9 + 7

# 桁DPを行う
# DP[k][b] k 桁の数字で, B で割った余りが b となるような数の個数
DP = [[0 for i in range(B)] for _ in range(N+1)]
DP[0][0] = 1

for k in range(1, N+1):
    for b in range(B):
        for c in C:
            b_ = (10 * b + c)%B
            DP[k][b_] += DP[k-1][b]
            DP[k][b_] %= MOD

print(DP[-1][0])