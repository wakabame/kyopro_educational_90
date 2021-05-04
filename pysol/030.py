N, K = map(int, input().split())


prime_count = [0] * (N + 1)
prime_count[0] = -1

for i in range(2, N + 1):
    if prime_count[i]:
        # 素数でないならスキップ
        continue
    curr = i
    while curr <= N:
        prime_count[curr] += 1
        curr += i

ans = 0
for i in range(N + 1):
    if prime_count[i] >= K:
        ans += 1
print(ans)
