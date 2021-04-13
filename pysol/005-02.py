import numpy as np
N, B, K = map(int, input().split())
C = list(map(int, input().split()))
MOD = 10 ** 9 + 7

# DP の漸化式が同じ場合は, 行列の繰り返し二乗法によって求めることができる
# numpy を使う場合は, np.int32 ではoverflowが起こるので, 'dtype=object' を指定する
# numpy 実装による高速化の恩恵がない？
def power_matrix_under_mod(mat, n, p):
    res = np.identity(B, dtype=object)
    bi = str(format(n, "b"))  # 2進表現に
    for i in range(len(bi)):
        res = np.dot(res, res)
        res = np.mod(res, p)
        if bi[i] == "1":
            res = np.dot(res, mat)
            res = np.mod(res, p)
    return res


# 行列の累乗を行う
dp_matrix = np.zeros((B, B), dtype=object)
for b in range(B):
    for c in C:
        b_ = (10 * b + c)%B
        dp_matrix[b][b_] += 1

print(power_matrix_under_mod(dp_matrix, N, MOD)[0][0])
