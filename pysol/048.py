N, K = map(int, input().split())
scores = []
for _ in range(N):
    a, b = map(int, input().split())
    scores += [b, a-b]

scores.sort(reverse=True)

print(sum(scores[:K]))
