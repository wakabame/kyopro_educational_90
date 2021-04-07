N = int(input())
path = [[] for i in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    path[a-1] += [b-1]
    path[b-1] += [a-1]

# 木の直径を出すには最短距離計算を2回行う
# 一度目は, 適当な頂点を根と見なして, そこから最も遠い頂点 = 直径の端点をみつける
# BFS でも DFS でもよい（以下はDFSで実装）
# 二度目は, その頂点から最短距離を計算し, 最も遠い頂点 = 直径ももう一端 との距離を算出
next_vec = [(0, 0)]
visited = [False] * N
distance_from_zero = [-1] * N
visited[0] = True
distance_from_zero[0] = 0

while next_vec:
    u, d = next_vec.pop()
    for v in path[u]:
        if visited[v]:
            continue
        distance_from_zero[v] = d+1
        visited[v] = True
        next_vec.append((v, d+1))

root_index = distance_from_zero.index(max(distance_from_zero))

next_vec = [(root_index, 0)]
visited = [False] * N
distance_from_zero = [-1] * N
visited[root_index] = True
distance_from_zero[root_index] = 0

while next_vec:
    u, d = next_vec.pop()
    for v in path[u]:
        if visited[v]:
            continue
        distance_from_zero[v] = d+1
        visited[v] = True
        next_vec.append((v, d+1))

print(max(distance_from_zero) + 1)