K = int(input())
MOD = 10**9+7
DP = [0] * (K+9)
DP[8] = 1

if K%9 != 0:
    exit(print(0))

for i in range(K):
    DP[i+9] = sum(DP[i:i+9]) % MOD

print(DP[-1])