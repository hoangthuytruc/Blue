INF = int(1e9)


def BellmanFord(s):
    dist[s] = 0
    for i in range(n - 1):
        for u, v, w in graph:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    for i in range(n - 1):
        for u, v, w in graph:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = -INF
    return dist


if __name__ == '__main__':
    while True:
        n, m, q, s = map(int, input().split())
        if n == 0 and m == 0 and q == 0 and s == 0:
            break

        dist = [INF] * n
        graph = []
        for _ in range(m):
            u, v, w = map(int, input().split())
            graph.append((u, v, w))
        path = BellmanFord(s)
        for _ in range(q):
            f = int(input())
            minPath = path[f]
            if minPath == -INF:
                print("-Infinity")
            elif minPath == INF:
                print("Impossible")
            else:
                print(minPath)
        print()