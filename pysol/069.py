MOD = 10**9+7
N, K = map(int, input().split())

if N == 1:
    exit(print(K%MOD))
if N == 2:
    exit(print((K*(K-1))%MOD))
if K == 1:
    exit(print(0))
if K == 2:
    exit(print(0))
ans = K * (K-1)
ans *= pow(K-2, N-2, MOD)

print(ans%MOD)
