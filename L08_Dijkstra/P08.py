from heapq import heappush, heappop
INF = int(1e9)


def Djikstra(s, dist, graph):
    pq = [(0, s)]
    dist[s] = 0

    while pq:
        w, u = heappop(pq)
        if w > dist[u]:
            continue
        for d, v in graph[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heappush(pq, (dist[v], v))


if __name__ == '__main__':
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        graph = [[] for _ in range(n)]
        graphS = [[] for _ in range(n)]
        graphD = [[] for _ in range(n)]

        dist = [INF] * n
        distS = [INF] * n
        distD = [INF] * n

        s, d = map(int, input().split())
        for _ in range(m):
            u, v, w = map(int, input().split())
            graphS[u].append((w, v))
            graphD[v].append((w, u))

        Djikstra(s, distS, graphS)
        Djikstra(d, distD, graphD)
        shortestPath = distS[d]

        for u in range(n):
            for w, v in graphS[u]:
                if distS[u] + w + distD[v] != shortestPath:
                    graph[u].append((w, v))
        Djikstra(s, dist, graph)
        print(dist[d] if dist[d] != INF else -1)