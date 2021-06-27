from collections import defaultdict

H, W = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(H)]

ans = 0
for j in range(1<<H):
    curr = 0
    di = defaultdict(int)
    for w in range(W):
        v_set = set()
        v_length = 0
        for k in range(H):
            if 1<<k & j :
                v_set.add(P[k][w])
                v_length += 1
        if len(v_set) == 1:
            di[v_set.pop()] += v_length
    if di:
        ans = max(ans, sorted(list(di.values()))[-1])

print(ans)
