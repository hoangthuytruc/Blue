def getroot(lab, u):
    if lab[u] == -1:
        return u
    lab[u] = getroot(lab, lab[u])
    return lab[u]

def union(lab, cou, a, b):
    if cou[a] > cou[b]:
        cou[a] += cou[b]
        lab[b] = a
    else:
        cou[b] += cou[a]
        lab[a] = b

def solve():
    n, m = map(int, input().split())
    lab = [-1 for _ in range(n)]
    cou = [1 for _ in range(n)]

    if n != m:
        print('NO')
        return
    for i in range(m):
        u, v = map(int, input().split())
        u = getroot(lab, u-1)
        v = getroot(lab, v-1)
        if u != v:
            union(lab, cou, u, v)
    if lab.count(-1) > 1:
        print('NO')
        return
    print('FHTAGN!')
solve()
