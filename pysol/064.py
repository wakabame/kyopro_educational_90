N, Q = map(int, input().split())
A = list(map(int, input().split()))
diff = [A[i+1] - A[i] for i in range(N-1)]

for _ in range(Q):
    l, r, v = map(int, input().split())
    if l > 1:
        diff[l-2] += v
    if r < N:
        diff[r-1] -= v
    print(sum([abs(d) for d in diff]))
