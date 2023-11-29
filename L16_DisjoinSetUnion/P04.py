import sys
sys.setrecursionlimit(100000)
MAX = 10000

def findSet(u):
    if u != parent[u]:
        parent[u] = findSet(parent[u])
    return parent[u]


def unionSet(u, v):
    up = findSet(u)
    vp = findSet(v)
    parent[vp] = up

if __name__ == '__main__':
    n = int(input())
    parent = [i for i in range(MAX * 2)]
    while True:
        c, x, y = map(int, input().split())
        if c == x == y == 0:
            break
        if c == 1:
            if findSet(x) == findSet(y + MAX):
                print(-1)
                continue
            unionSet(x, y)
            unionSet(x + MAX, y + MAX)
        if c == 2:
            if findSet(x) == findSet(y):
                print(-1)
                continue
            unionSet(x, y + MAX)
            unionSet(x + MAX, y)
        if c == 3:
            if findSet(x) == findSet(y):
                print(1)
            else:
                print(0)
        if c == 4:
            if findSet(x) == findSet(y + MAX):
                print(1)
            else:
                print(0)