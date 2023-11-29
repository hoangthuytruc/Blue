from queue import PriorityQueue
MAX = 100001
root = [0] * MAX
cnt = [0] * MAX
maxi = 1
pq = PriorityQueue()

def findRoot(u):
    if u == root[u]:
        return u
    root[u] = findRoot(root[u])
    return root[u]

def unionSet(u, v):
    global maxi

    uu = findRoot(u)
    vv = findRoot(v)

    if uu != vv:
        cnt[uu] += cnt[vv]
        root[vv] = uu
        pq.put((cnt[uu], uu))
        maxi = max(maxi, cnt[uu])

if __name__ == '__main__':
    n, m = map(int, input().split())
    for i in range(1, n + 1):
        cnt[i] = 1
        root[i] = i
        pq.put((1, i))
    for i in range(m):
        u, v = map(int, input().split())
        unionSet(u, v)
        while True:
            tmp = pq.queue[0]
            r = findRoot(tmp[1])
            if r != tmp[1]:
                pq.get()
                continue
            if cnt[r] != tmp[0]:
                pq.get()
                continue
            break
        print(maxi - pq.queue[0][0])