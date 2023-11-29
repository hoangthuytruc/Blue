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

if __name__ == '__main__':
    n = int(input())
    x = [0 for _ in range(n)]
    y = [0 for _ in range(n)]
    for i in range(n):
        x[i], y[i] = map(int, input().split())
    lab = [-1 for _ in range(n)]
    cou = [1 for i in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j]:
                u = getroot(lab, i)
                v = getroot(lab, j)
                if u != v:
                    union(lab, cou, u, v)
    print(lab.count(-1) - 1)