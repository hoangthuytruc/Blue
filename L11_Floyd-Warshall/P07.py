MAX = 49

if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        dist = [[0 for _ in range(MAX)] for _ in range(MAX)]
        for _ in range(n):
            s, e, c = map(int, input().split())
            dist[s][e] = max(dist[s][e], c)

        for k in range(MAX):
            for i in range(MAX):
                for j in range(MAX):
                    if i <= k <= j:
                        dist[i][j] = max(dist[i][j], dist[i][k] + dist[k][j])
        print(dist[0][MAX - 1])