n = int(input())
dist = [[0] * (n + 1)]

for i in range(1, n + 1):
    dist.append([0] + list(map(int, input().split())))

middleV = list(map(int, input().split()))
res = [0] * n

for idx in range(n - 1, -1, -1):
    k = middleV[idx]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    for u in middleV[idx:]:
        for v in middleV[idx:]:
            res[idx] += dist[u][v]
print(*res)