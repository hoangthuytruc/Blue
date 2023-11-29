import queue
INF = 1e9
class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id

    def __lt__(self, other):
        return self.dist <= other.dist

def prims(src):
    pq = queue.PriorityQueue()
    pq.put(Node(src, 0))
    dist[src] = 0
    while not pq.empty():
        top = pq.get()
        u = top.id
        visited[u] = True
        for neighbor in graph[u]:
            v = neighbor.id
            w = neighbor.dist
            if not visited[v] and w < dist[v]:
                dist[v] = w
                pq.put(Node(v, w))
                path[v] = u

def getWeight():
    ans = 0
    for i in range(n + 1):
        if path[i] == -1:
            continue
        ans += dist[i]
    return ans


if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        p = int(input())
        n = int(input())
        m = int(input())

        graph = [[] for _ in range(n + 1)]
        dist = [INF for _ in range(n + 1)]
        visited = [False for _ in range(n + 1)]
        path = [-1 for _ in range(n + 1)]

        for i in range(m):
            u, v, w = map(int, input().split())
            graph[u].append(Node(v, w))
            graph[v].append(Node(u, w))
        prims(1)
        print(getWeight() * p)