N, K = map(int, input().split())
XY = [tuple(map(int, input().split())) for _ in range(N)]


def culc_dist(i, j):
    ret = (XY[i][0] - XY[j][0]) ** 2 + (XY[i][1] - XY[j][1]) ** 2
    return ret


def bit_number_to_list(bit_number):
    ret = []
    for i in range(N):
        ret += [bit_number%2]
        bit_number //= 2
    return ret


def bit_ls_to_number(bit_ls):
    ret = 0
    for i in range(N)[::-1]:
        ret += bit_ls[i]
        ret *= 2
    ret //= 2
    return ret

# d[bit] ... グループに含まれる点の集合がbitのときの2点間の距離の最大値
d = [0 for i in range(1<<N)]
for bit in range(1<<N):
    # d[bit] を更新する
    bit_ls = bit_number_to_list(bit)
    for i in range(N)[::-1]:
        # i 番目のフラグを立てるとき, それ以外のフラグが立っているものを見る
        if bit_ls[i] and i != 0:
            pre_bit_ls = bit_ls[:i] + [0] * (N-i)
            curr = 0
            for j in range(N):
                if pre_bit_ls[j]:
                    curr = max(curr, culc_dist(i, j))

            d[bit_ls_to_number(bit_ls)] = max(d[bit_ls_to_number(pre_bit_ls)], curr)
            break

DP = [[10**18 for _ in range(1<<N)] for _ in range(K+1)]
DP[0][0] = 0
# DP[k][bit] ... すでに選んだ点 bit, 現在のグループ数 k に対するスコアの最小値
for k in range(K):
    # 要素 N の集合について, 部分集合 bit とその部分集合 subbit を列挙するのは O(3^N)
    # ナイーブにやると O(4^N) だが, (subbit - 1) & bit により「繰り下がりの引き算」を行う
    for bit in range(1<<N):
        subbit = bit
        curr = 10**18
        # bit の部分集合 subbit を列挙する
        while subbit:
            subbit = (subbit - 1) & bit

            curr = min(curr, max(DP[k][subbit], d[bit - subbit]))
        DP[k+1][bit] = curr

print(DP[-1][-1])
