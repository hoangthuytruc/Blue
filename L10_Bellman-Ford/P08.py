def BellmanFord(s, n, dist, graph):
    dist[s] = 0
    for i in range(n - 1):
        for edge in graph:
            u, v, w = edge
            dist[v] = min(dist[v], dist[u] + w)

n = int(input())
dist = [10 ** 9] * (n + 1)
graph = []

for i in range(2, n + 1):
    line = input().split()
    for j in range(1, i):
        if line[j - 1] != 'x':
            w = int(line[j - 1])
            graph.append((j, i, w))
            graph.append((i, j, w))
BellmanFord(1, n, dist, graph)

res = 0
for i in range(1, n + 1):
    res = max(res, dist[i])
print(res)