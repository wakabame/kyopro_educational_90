import numba

N = int(input())
A = list(map(int, input().split()))

A.sort()
a, b, c = A
b = b - a
c = c - a


@numba.jit
def solve():
    for K in range(10000 + 1):
        # 合計 K 枚のコインで払えるか
        n = N - K * a
        for i in range(K + 1):  # cを使う枚数
            nn = n - c * i
            if nn % b == 0 and 0 <= nn // b <= (K - i):
                return K


print(solve())
