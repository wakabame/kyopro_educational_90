# キーワード: Grundy 数, Nim
# 終端状態で負けとなるゲームにおいては、必ず負ける状態と、そうでない状態がある
# 必ず負ける状態のGrundy数を0であり、各状態の Grundy 数を遷移先のGrundyのmexとなるように再帰的に定義したとき、
# 並列ゲーム Nim は各ゲームのGrundy数のxorが0のとき後手勝ち、そうでないとき先手勝ちとなる
N = int(input())
W = list(map(int, input().split()))
B = list(map(int, input().split()))

# Grundy数を計算する
# ある状態の Grundy数 = 遷移先の Grundy数たちのmex
grundy = [[-1 for _ in range(1326)] for _ in range(51)]
grundy[0][1] = 0

# 前処理としての計算
for w in range(51):
    for b in range(1326):
        if w * (w + 1) // 2 + b >= 1326 or w < 0:
            continue
        mex_table = [0] * 2000
        mex_table[grundy[w - 1][b + w]] += 1
        for b_ in range(b - b // 2, b):
            mex_table[grundy[w][b_]] += 1
        for i in range(2000):
            if mex_table[i] == 0:
                grundy[w][b] = i
                break

# Nim数を出す。後手が勝てる ＝ 全ての山のGroundy数たちのxor が0
ans = 0
for i in range(N):
    ans ^= grundy[W[i]][B[i]]

if ans:
    print("First")
else:
    print("Second")
