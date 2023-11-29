INF = 10 ** 9


def FloydWarshall(dist):
    for _ in range(2):
        for k in range(1, n + 1):
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    maxFeast = max(maxCost[i][k], maxCost[k][j])
                    if dist[i][j] + maxCost[i][j] > dist[i][k] + dist[k][j] + maxFeast:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        maxCost[i][j] = maxFeast


if __name__ == '__main__':
    tc = 1
    while True:
        n, m, q = map(int, input().split())
        if n == 0:
            break

        c = [0] + list(map(int, input().split()))
        maxCost = [[None for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                maxCost[i][j] = max(c[i], c[j])

        dist = [[0 if i == j else INF for j in range(n + 1)] for i in range(n + 1)]
        for _ in range(m):
            u, v, d = map(int, input().split())
            dist[u][v] = d
            dist[v][u] = d
        FloydWarshall(dist)
        if tc > 1:
            print()

        print("Case #{}".format(tc))
        tc += 1
        for _ in range(q):
            s, d = map(int, input().split())
            print(-1 if dist[s][d] == INF else dist[s][d] + maxCost[s][d])