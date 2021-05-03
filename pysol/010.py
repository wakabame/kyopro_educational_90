N = int(input())
A, B = [0], [0]
for _ in range(N):
    c, p = map(int, input().split())
    if c == 1:
        A += [A[-1] + p]
        B += [B[-1]]
    if c == 2:
        A += [A[-1]]
        B += [B[-1] + p]

Q = int(input())

for _ in range(Q):
    l, r = map(int, input().split())
    print(A[r] - A[l - 1], B[r] - B[l - 1])
