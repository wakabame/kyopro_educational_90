N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

def is_ok(mid):
    # 今のピースを追加したら mid 以上になる場合には分割するようにする
    # 分割階数が K 未満なら False
    last = 0
    separate = 0
    for i in range(N):
        if A[i] - last >= mid and L - A[i] >= mid:
            separate += 1
            last = A[i]
    if separate >= K:
        return True
    else:
        return False

# 汎用的な二分探索のテンプレ
def binary_search(ok, ng):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

ok = 0
ng = 10**5

print(binary_search(ok, ng) )