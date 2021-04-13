N = int(input())
A = list(map(int, input().split()))
Q = int(input())

A.sort()


def is_ok(mid, b):
    # A[mid] < b なら OK 出す
    return A[mid] < b

# 汎用的な二分探索のテンプレ
def binary_search(ok, ng, b):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid, b):
            ok = mid
        else:
            ng = mid
    return ok

for _ in range(Q):
    b = int(input())
    ok = -1
    ng = len(A)
    best_index = binary_search(ok, ng, b)
    if best_index < len(A) - 1:
        print(min(abs(b - A[best_index]), abs(b- A[best_index+1])))
    else:
        print(abs(b - A[best_index]))
