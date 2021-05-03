N = int(input())
A = list(map(int, input().split()))

# 区間DPにより答えを出す
# dp[i][j]: i から j までの区間 [i,j] での最良スコア
# dp[0][2*N-1] が答えになる
dp = [[float("inf") for _ in range(2 * N)] for _ in range(2 * N)]
for i in range(2 * N - 1):
    dp[i][i + 1] = abs(A[i + 1] - A[i])


for h in range(2, 2 * N):  # 幅 h = j - i について考える
    for i in range(2 * N - h):
        j = i + h
        """
        dp[i][j] の候補は4パターン
        dp[i][i+1] + dp[i+2][j] # 左端に追加
        dp[i][j-2] + dp[j-1][j] # 右端に追加
        dp[i+1][j-1] + abs(A[j] - A[i]) # i,j のペアを最後に作る
        dp[i][k] + dp[k+1][j] " 二つの区間の和
        """
        dp[i][j] = min(
            dp[i][i + 1] + dp[i + 2][j],
            dp[i][j - 2] + dp[j - 1][j],
            dp[i + 1][j - 1] + abs(A[j] - A[i]),
        )
        for k in range(i, j):  # [i,j] を [i,k], [k+1, j] に分割する
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])

print(dp[0][-1])
