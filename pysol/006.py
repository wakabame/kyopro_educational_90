from collections import deque
N, K = map(int, input().split())
S = input()

# 今 K のうち k 文字目を決めるとき
# S の 0 文字目から|S| - k 文字目までのもののなかで, "a" に近いものを採用する
# さらに, その位置に移動する.
q = deque()

ans = ""
for i, c in enumerate(S):
    while q and q[-1] > c:
        q.pop()
    q.append(c)
    if i >= N - K:
        ans += q.popleft()

print(ans)
