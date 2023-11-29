def find(u):
    global par
    if u != par[u]:
        par[u] = find(par[u])
    return par[u]

def union(u, v):
    u = find(u)
    v = find(v)
    par[u] = v

if __name__ == '__main__':
    n, a, b = map(int, input().split())
    p = list(map(int, input().split()))
    mp = dict()
    for i in range(n):
        mp[p[i]] = i + 1
    par = [i for i in range(n + 2)]
    for i in range(n):
        union(i + 1, mp.get(a - p[i], n + 1))
        union(i + 1, mp.get(b - p[i], 0))
    A = find(0)
    B = find(n + 1)
    if A != B:
        print('YES')
        print(' '.join(['1' if find(i) == B else '0' for i in range(1, n + 1)]))
    else:
        print('NO')