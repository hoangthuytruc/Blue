parent = []
rank = []


def makeSet():
    global parent, rank
    parent = [i for i in range(n + 1)]
    rank = [0 for _ in range(n + 1)]


def findSet(u):
    if parent[u] != u:
        parent[u] = findSet(parent[u])
    return parent[u]


def unionSet(u, v):
    up = findSet(u)
    vp = findSet(v)

    if up == vp:
        return
    if rank[up] > rank[vp]:
        parent[vp] = up
    elif rank[up] < rank[vp]:
        parent[up] = vp
    else:
        parent[up] = vp
        rank[vp] += 1


if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        n, m = map(int, input().split())
        makeSet()

        for i in range(m):
            u, v = map(int, input().split())
            unionSet(u, v)

        count = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            p = findSet(i)
            count[p] += 1
        print(max(count))