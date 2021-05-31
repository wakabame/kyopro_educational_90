MOD = 10 ** 9 + 7
N = int(input())
A = [sum(map(int, input().split())) for _ in range(N)]

ans = 1
for a in A:
    ans *= a
    ans %= MOD
print(ans)
