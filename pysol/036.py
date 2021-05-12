N, Q = map(int, input().split())
positive = []
negative = []

for _ in range(N):
    x, y = map(int, input().split())
    positive += [x + y]
    negative += [x - y]

p = [max(positive), min(positive)]
q = [max(negative), min(negative)]

for _ in range(Q):
    i = int(input()) - 1
    curr = 0
    p_ = positive[i]
    curr = max(curr, abs(p_ - p[0]))
    curr = max(curr, abs(p_ - p[1]))
    q_ = negative[i]
    curr = max(curr, abs(q_ - q[0]))
    curr = max(curr, abs(q_ - q[1]))

    print(curr)
