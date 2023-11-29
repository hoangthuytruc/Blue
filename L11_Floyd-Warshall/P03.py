def FloydWarshall(dist):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = max(dist[i][j], dist[i][k] * dist[k][j])


def isPossible(dist):
    for i in range(n):
        if dist[i][i] > 1:
            return True
    return False


if __name__ == '__main__':

    tc = 0
    while True:
        tc += 1
        n = int(input())
        if n == 0:
            break
        currencies = dict()
        for i in range(n):
            currencies[input()] = i

        m = int(input())
        dist = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        for _ in range(m):
            a, r, b = input().split()
            dist[currencies[a]][currencies[b]] = float(r)
        FloydWarshall(dist)
        if isPossible(dist):
            print("Case {}: Yes".format(tc))
        else:
            print("Case {}: No".format(tc))
        input()