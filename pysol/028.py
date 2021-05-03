N = int(input())

table = [[0 for i in range(1001)] for _ in range(1001)]
for _ in range(N):
    a, b, c, d = map(int, input().split())
    table[a][b] += 1
    table[c][b] -= 1
    table[a][d] -= 1
    table[c][d] += 1

cumsum_table = [[0 for i in range(1001)] for _ in range(1001)]

for i in range(1001):
    for j in range(1001):
        cumsum_table[i][j] += table[i][j]
        if i > 0:
            cumsum_table[i][j] += cumsum_table[i - 1][j]
        if j > 0:
            cumsum_table[i][j] += cumsum_table[i][j - 1]
        if i > 0 and j > 0:
            cumsum_table[i][j] -= cumsum_table[i - 1][j - 1]


ans = [0 for i in range(N + 1)]
for i in range(1001):
    for j in range(1001):
        ans[cumsum_table[i][j]] += 1

for i in range(1, N + 1):
    print(ans[i])
