N, K = map(int, input().split())
A = list(map(int, input().split()))

from collections import defaultdict

d = defaultdict(int)
k = 0
start, end = 0, 0
ans = 0

# [start, end) の区間での変数の種類数 k と, 区間に含まれる変数ごとの個数 d を管理する
while start < N:
    if start == end:
        # 区間幅が0の場合
        end += 1
        k = 1
        d[A[start]] += 1
    elif end < N and (k < K or d[A[end]] > 0):
        # 伸ばせる場合
        end += 1
        if d[A[end - 1]] == 0:
            k += 1
        d[A[end - 1]] += 1
    else:
        # 縮める場合
        start += 1
        if d[A[start - 1]] == 1:
            k -= 1
        d[A[start - 1]] -= 1
    ans = max(ans, end - start)

print(ans)
