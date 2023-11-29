import queue
INF = int(1e9)


def Djikstra(s, graph):
    dist = [INF for _ in range(n + 1)]
    dist[s] = 0
    pq = queue.PriorityQueue()
    pq.put((0, s))

    while not pq.empty():
        top = pq.get()
        for v in graph[top[1]]:
            if top[0] + v[0] < dist[v[1]]:
                dist[v[1]] = top[0] + v[0]
                pq.put((dist[v[1]], v[1]))
    return dist


if __name__ == '__main__':
    Q = int(input())
    for _ in range(Q):
        n, m, k, s, t = map(int, input().split())
        graphS = [[] for i in range(n + 1)]
        graphT = [[] for i in range(n + 1)]
        for _ in range(m):
            d, c, l = map(int, input().split())
            graphS[d].append((l, c))
            graphT[c].append((l, d))
        s_dist = Djikstra(s, graphS)
        t_dist = Djikstra(t, graphT)

        new_dist = []
        for _ in range(k):
            u, v, q = map(int, input().split())
            new_min = min(s_dist[t], (s_dist[u] + q + t_dist[v]), (s_dist[v] + q + t_dist[u]))
            if new_min == INF:
                new_min = -1
            new_dist.append(new_min)
        print(min(new_dist))