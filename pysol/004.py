H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

H_table = [sum(a) for a in A]
W_table = [0] * W
for a in A:
    for w in range(W):
        W_table[w] += a[w]

for h in range(H):
    print(*[H_table[h] + W_table[w] - A[h][w] for w in range(W)])
