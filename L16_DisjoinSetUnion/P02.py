parent = []
rank = []


def makeSet():
    global parent, rank
    parent = [i for _ in range(n)]
    rank = [0 for _ in range(n)]


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


def getIndex(c):
    return ord(c) - ord('A')


if __name__ == '__main__':
    lines = []
    while True:
        try:
            lines.append(input())
        except EOFError:
            break
    len_input = len(lines)
    k = 0
    tc = int(lines[k])
    k += 1
    for t in range(tc):
        k += 1
        x = list(lines[k])[0]
        n = getIndex(x) + 1
        while k < len_input and lines[k] != '\n':
            tmp = list[lines[k]]
            u = getIndex(tmp[0])
            v = getIndex(tmp[1])
            k += 1
            u = findSet(u)
            v = findSet(v)
            if u != v:
                unionSet(u, v)
        cnt = 0
        for i in range(n):
            if i == parent[i]:
                cnt += 1
        if t == tc - 1:
            print(cnt)
        else:
            print("{}\n".format(cnt))