MAX = 50
INF = int(1e9)

def FloyWarShall():
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

T = int(input())
for _ in range(T):
    s = input()
    V = len(s)
    dist = [[0] * V for _ in range(V)]
    matrix = []
    for i in range(V):
        if i == 0:
            matrix.append(s)
        else:
            matrix.append(input())
        for j in range(V):
            if matrix[i][j] == 'Y':
                dist[i][j] = 1
            elif i == j:
                dist[i][j] = 0
    FloyWarShall()
    nfriends, index = 0, 0
    for i in range(V):
        count = 0
        for j in range(V):
            if dist[i][j] == 2:
                count += 1

            if count > nfriends:
                nfriends = count
                index = i
    print(index, nfriends)
