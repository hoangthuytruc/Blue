INF = int(1e9)


def BellmanFord(s):
    dist[s] = 0
    for _ in range(n - 1):
        for u, v, w in graph:
            if dist[u] != -INF and dist[u] + w > dist[v]:
                dist[v] = dist[u] + w

    for u, v, w in graph:
        if dist[u] != -INF and dist[u] + w > dist[v]:
            return True
    return False


if __name__ == '__main__':
    Q = int(input())
    for _ in range(Q):
        n, m = map(int, input().split())
        dist = [-INF] * (n + 1)
        graph = []
        for _ in range(m):
            u, v, w = map(int, input().split())
            graph.append((u, v, w))
        hasPositiveCycle = BellmanFord(1)
        print("Yes" if hasPositiveCycle else "No")
