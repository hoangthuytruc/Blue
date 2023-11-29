import queue
INF = 1e9

def prime(src):
    pq = queue.PriorityQueue()
    dist[src] = 0
    pq.put((0, src))
    while not pq.empty():
        u = pq.get()
        visited[u[1]] = True
        for w, v in graph[u[1]]:
            if not visited[v] and dist[v] > w:
                dist[v] = w
                path[v] = u
                pq.put((w, v))
    minDist = list()
    for i in range(1, n + 1):
        if path[i] != -1:
            minDist.append(dist[i])
    return minDist

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    dist = [INF] * (n + 1)
    path = [-1] * (n + 1)

    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((w, v))
        graph[v].append((w, u))
    old_cables = prime(1)
    q = int(input())
    new_cables = list(map(int, input().split()))

    new_cables.sort()
    old_cables.sort()
    i = 0
    j = len(old_cables) - 1
    while i < q and j >= 0:
        if old_cables[j] > new_cables[i]:
            old_cables[j] = new_cables[i]
            i += 1
        j -= 1
    print(sum(old_cables))