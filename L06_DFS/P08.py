def DFS(src):
    global leaf, max_dist
    dist = [-1] * (V + 1)
    s = [src]
    dist[src] = 0

    while len(s):
        u = s.pop()
        for v, w in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + w
                max_dist = max(max_dist, dist[v])
                s.append(v)
    leaf = dist.index(max(dist))


t = int(input())
for _ in range(t):
    V = int(input())
    E = V - 1
    graph = [[] for _ in range(V+1)]

    for i in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    leaf = 0
    max_dist = 0
    DFS(1)
    DFS(leaf)

    print(max_dist)