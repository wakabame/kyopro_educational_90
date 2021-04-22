# 強連結成分分解
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components
from collections import Counter


N, M = map(int, input().split())

edge = np.array([input().split() for _ in range(M)], dtype=np.int64).T
tmp = np.ones(M, dtype=np.int64).T
graph = csr_matrix((tmp, (edge[:]-1)), (N, N))

component_count, labels = connected_components(graph, directed=True, connection='strong')

ans = sum([v*(v-1)//2 for v in Counter(labels).values()])
print(ans)
