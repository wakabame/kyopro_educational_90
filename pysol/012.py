# グラフの連結を union-find を使って判定する
from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.red = [False] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

def get_number(xy):
    x, y = xy
    return (x-1)*W + (y-1)

def get_neighbors(xy):
    x, y = xy
    ret = []
    if x > 1:
        ret += [get_number((x-1, y))]
    if x < H:
        ret += [get_number((x+1, y))]
    if y > 1:
        ret += [get_number((x, y-1))]
    if y < W:
        ret += [get_number((x, y+1))]
    return ret

H, W = map(int, input().split())
Q = int(input())

uf = UnionFind(H*W)

for _ in range(Q):
    t, *q = map(int, input().split())
    if t == 1:
        n = get_number(q)
        uf.red[n] = True
        neighbor_nums = get_neighbors(q)
        for k in neighbor_nums:
            if uf.red[k]:
                uf.union(n, k)
    elif t == 2:
        xa, ya, xb, yb = q
        a = get_number((xa, ya))
        b = get_number((xb, yb))
        if uf.same(a, b) and uf.red[a]:
            print("Yes")
        else:
            print("No")
