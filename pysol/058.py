from collections import defaultdict
N, K = map(int, input().split())

# 値が何回目に現れたかをメモする
d = defaultdict(int)
d[N] = 0


def bottun(N):
    table = [int(i) for i in str(N)]
    for i in table:
        N += i
    return N%(10**5)


for i in range(1, K + 1):
    # i ボタンを押した回数
    N = bottun(N)
    if N in d:
        period = i - d[N]
        rem = (K - i)%period
        for p in range(rem):
            N = bottun(N)
        exit(print(N))
    d[N] = i
print(N)
