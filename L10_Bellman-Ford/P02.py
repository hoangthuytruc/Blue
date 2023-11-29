INF = int(1e9)


def BellmanFord(s):
    dist = [INF] * (V + 1)
    dist[s] = 0
    for i in range(1, V):
        for j in range(E):
            u, v, w = graph[j]
            if (dist[u] != INF) and (dist[u] + w < dist[v]):
                dist[v] = dist[u] + w

    for i in range(E):
        u, v, w = graph[j]
        if (dist[u] != INF) and (dist[u] + w < dist[v]):
            return [INF] * (V+1)
    return dist


if __name__ == '__main__':
    Q = int(input())
    for i in range(Q):
        print("Case {0}:".format(i + 1))
        _ = input()
        V = int(input())
        weights = list(map(int, input().split()))
        E = int(input())
        graph = []
        for i in range(E):
            u, v = map(int, input().split())
            graph.append((u, v, pow(weights[v-1] - weights[u-1], 3)))
        queries = int(input())
        dist = BellmanFord(1)
        for i in range(queries):
            f = int(input())
            print(dist[f] if dist[f] != INF and dist[f] > 2 else "?")