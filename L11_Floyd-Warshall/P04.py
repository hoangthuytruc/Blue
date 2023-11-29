INF = 10 ** 9

def FloydWarshall(dist):
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


if __name__ == '__main__':
    tc = 0
    n = 20
    while True:
        try:
            dist = [[INF for j in range(n + 1)] for i in range(n + 1)]
            for i in range(1, n):
                for j in list(map(int, input().split()))[1:]:
                    dist[i][j] = dist[j][i] = 1
            FloydWarshall(dist)
            tc += 1
            print("Test Set #{}".format(tc))
            m = int(input())
            for _ in range(m):
                u, v = map(int, input().split())
                print("{:2d} to {:2d}: {}".format(u, v, dist[u][v]))
            print()
        except EOFError:
            break
