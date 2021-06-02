N, P, Q = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for i1 in range(N):
    for i2 in range(i1):
        for i3 in range(i2):
            for i4 in range(i3):
                for i5 in range(i4):
                    curr = 1
                    curr *= A[i1]
                    curr %= P
                    curr *= A[i2]
                    curr %= P
                    curr *= A[i3]
                    curr %= P
                    curr *= A[i4]
                    curr %= P
                    curr *= A[i5]
                    curr %= P
                    if curr == Q:
                        ans += 1
print(ans)
