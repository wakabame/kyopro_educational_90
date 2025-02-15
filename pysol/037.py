W, N = map(int, input().split())


class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(N)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """

    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


L, R, V = [], [], []
for _ in range(N):
    l, r, v = map(int, input().split())
    L += [l]
    R += [r]
    V += [v]

# dp[i][w] ... i 個の料理までを見たとき, 調味料 w で作れる料理の価値の最大値
dp = [[-(10 ** 12) for _ in range(W + 1)] for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):  # i番目の
    old_segtree = SegTree(dp[i], max, -float("INF"))
    for w in range(W + 1):
        l = max(0, w - R[i])
        r = max(0, w - L[i] + 1)
        if l == r == 0:
            dp[i + 1][w] = dp[i][w]
        else:
            dp[i + 1][w] = max(dp[i][w], old_segtree.query(l, r) + V[i])

if dp[-1][-1] < 0:
    print(-1)
else:
    print(dp[-1][-1])
