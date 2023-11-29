import queue
INF = int(1e9)


def Djikstra(s):
    dist = [INF for _ in range(n)]
    dist[s] = 0
    pq = queue.PriorityQueue()
    pq.put((0, s))

    while not pq.empty():
        top = pq.get()
        if top[0] > dist[top[1]]:
            continue

        for v in graph[top[1]]:
            if top[0] + v[0] < dist[v[1]]:
                dist[v[1]] = top[0] + v[0]
                pq.put((dist[v[1]], v[1]))

    return dist


if __name__ == '__main__':
    Q = int(input())
    for i in range(Q):
        n = int(input())
        m = int(input())

        graph = [[] for _ in range(n)]
        for _ in range(m):
            u, v = map(int, input().split())
            graph[u].append((1, v))
            graph[v].append((1, u))

        s, t = map(int, input().split())
        s_dist = Djikstra(s)
        t_dist = Djikstra(t)

        res = 0
        for j in range(n):
            res = max(res, s_dist[j] + t_dist[j])

        print("Case {}: {}".format(i + 1, res))