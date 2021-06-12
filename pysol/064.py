N, Q = map(int, input().split())
A = list(map(int, input().split()))
diff = [A[i+1] - A[i] for i in range(N-1)]
ans = sum([abs(d) for d in diff])

for _ in range(Q):
    l, r, v = map(int, input().split())
    if l > 1:
        ans -= abs(diff[l-2])
        diff[l-2] += v
        ans += abs(diff[l-2])
    if r < N:
        ans -= abs(diff[r-1])
        diff[r-1] -= v
        ans += abs(diff[r-1])
    print(ans)
