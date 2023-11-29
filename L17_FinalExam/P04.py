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
    p, n = map(int, input().split())
    for _ in range(p):
        line = map(int, input().split())
        for d in range(len(line[1:])):
            unionSet()
