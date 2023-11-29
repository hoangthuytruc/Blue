from math import sqrt

INF = 10 ** 9

def FloyWarshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


def getDistance(a, b):
     return sqrt(pow(b[0] - a[0], 2) + pow(b[1] - a[1], 2))


if __name__ == '__main__':
    tc = int(input())
    for t in range(1, tc + 1):
        n = int(input())
        dist = [[0 if i == j else INF for j in range(n)] for i in range(n)]
        towns = []
        for i in range(n):
            x, y = map(int, input().split())
            towns.append((x, y, i))
        for a in towns:
            for b in towns:
                d = getDistance(a, b)
                if d <= 10:
                    dist[a[2]][b[2]] = d
                    dist[b[2]][a[2]] = d

        FloyWarshall()
        if t > 1:
            print()

        print("Case #{}:".format(t))
        maxDistance = -INF
        for a in towns:
            for b in towns:
                maxDistance = max(maxDistance, dist[a[2]][b[2]])
        print('{:.4f}'.format(maxDistance) if maxDistance != INF else "Send Kurdy")

