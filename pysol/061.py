Q = int(input())
# 上に入れる=l1の末尾に入れる
l1, l2 = [], []

for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        l1.append(x)
    elif t == 2:
        l2.append(x)
    else:
        if x <= len(l1):
            print(l1[-x])
        else:
            print(l2[x-len(l1)-1])
