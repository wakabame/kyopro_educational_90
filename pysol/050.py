MOD = 10 ** 9 + 7
N, L = map(int, input().split())

# dp[n] ... n 段目に辿りつく通り数
dp = [0] * (N + 1)
dp[0] = 1
for n in range(1, N+1):
    dp[n] = dp[n-1]
    if n >= L:
        dp[n] += dp[n-L]
        dp[n] %= MOD

print(dp[-1])
