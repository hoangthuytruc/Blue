import queue
INF = int(1e9)


def Djistra(s, f, graph, n):
    dist = [INF for _ in range(n)]
    dist[s] = 0
    pq = queue.PriorityQueue()
    pq.put((0, s))

    while not pq.empty():
        top = pq.get()
        for v in graph[top[1]]:
            if top[0] + v[0] < dist[v[1]]:
                dist[v[1]] = top[0] + v[0]
                pq.put((dist[v[1]], v[1]))
    return dist[f] if dist[f] != INF else "unreachable"


if __name__ == '__main__':
    Q = int(input())
    for i in range(Q):
        n, m, s, t = map(int, input().split())
        graph = [[] for _ in range(n)]
        for _ in range(m):
            u, v, w = map(int, input().split())
            graph[u].append((w, v))
            graph[v].append((w, u))
        print("Case #{0}: {1}".format(i + 1, Djistra(s, t, graph, n)))