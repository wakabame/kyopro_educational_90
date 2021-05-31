from collections import defaultdict
N = int(input())
A = [0] * 46
B = [0] * 46
C = [0] * 46
for a in map(int, input().split()):
    A[a%46] += 1
for b in map(int, input().split()):
    B[b%46] += 1
for c in map(int, input().split()):
    C[c%46] += 1

ans = 0
for a in range(46):
    for b in range(46):
        for c in range(46):
            if (a + b + c) % 46 == 0:
                ans += A[a] * B[b] * C[c]

print(ans)
