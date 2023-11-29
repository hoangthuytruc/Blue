from math import sqrt


def getDistance(x, y):
    return sqrt(pow(x, 2) + pow(y, 2))


if __name__ == '__main__':
    n, s = map(int, input().split())
    graph = []
    for i in range(n):
        x, y, p = map(int, input().split())
        d = getDistance(x, y)
        graph.append((d, p))
    graph.sort()
    res = -1
    for d in graph:
        s += d[1]
        if s >= 1000000:
            res = '{:.7f}'.format(d[0])
            break
    print(res)