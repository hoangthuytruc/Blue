import queue
INF = int(1e9)


def Djikstra(s):
    pq = queue.PriorityQueue()
    pq.put((0, s))
    dist = [INF for _ in range(n+1)]
    dist[s] = 0

    while not pq.empty():
        top = pq.get()
        if top[0] > dist[top[1]]:
            continue

        for v in graph[top[1]]:
            if v[0] + top[0] < dist[v[1]]:
                dist[v[1]] = v[0] + top[0]
                pq.put((dist[v[1]], v[1]))

    return dist


if __name__ == '__main__':
    n, m, k, x = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    chocolate = list(map(int, input().split()))
    for i in range(m):
        u, v, d = map(int, input().split())
        graph[u].append((d, v))
        graph[v].append((d, u))
    s, f = map(int, input().split())
    distS = Djikstra(s)
    distF = Djikstra(f)
    res = INF
    if distS[f] != INF:
        for c in chocolate:
            if distS[c] < x and distS[c] != INF and distF[c] != INF:
                res = min(res, distS[c] + distF[c])
        print(res if res != INF else "-1")
    else:
        print("-1")
