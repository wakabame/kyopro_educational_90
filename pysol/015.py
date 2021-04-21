N = int(input())

P = 10**9 + 7
fac = [1] + [1]
finv = [1] + [1]
inv = [0] + [1]

for i in range(2, N+1):
    fac += [fac[-1] * i % P]
    inv += [P - inv[P%i] * (P // i) %P]
    finv += [finv[-1] * inv[i] % P]


def comb(n, k):
    if n < 0 or k < 0 or n < k:
        return 0
    return fac[n] * finv[k] * finv[n-k] % P


def solve():
    for k in range(1, N+1):
        ans = 0
        a = 1
        while a <= N:
            ans += comb(N - (k-1) * (a-1),a)
            ans %= P
            a += 1
            if N < (k-1) * (a-1):
                break
        print(ans)

solve()
