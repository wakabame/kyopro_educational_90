N, Q = map(int, input().split())
A = list(map(int, input().split()))

cersor = 0
for _ in range(Q):
    T, x, y = map(int, input().split())
    if T == 1:
        x = (x-1+cersor)%N
        y = (y-1+cersor)%N
        A[x], A[y] = A[y], A[x]
    if T == 2:
        cersor -= 1
    if T == 3:
        print(A[(x-1+cersor)%N])
