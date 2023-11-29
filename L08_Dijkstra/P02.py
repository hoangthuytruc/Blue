import queue
MAX = 105
INF = int(1e9)
graph = [[] for _ in range(MAX)]
dist = [INF for _ in range(MAX)]


class Node:
    def __init__(self, _id, _weight):
        self.id = _id
        self.weight = _weight

    def __lt__(self, other):
        return self.weight < other.weight


def Dijkstra(s):
    pq = queue.PriorityQueue()
    pq.put(Node(s, 0))
    dist[s] = 0

    while not pq.empty():
        top = pq.get()
        u = top.id
        w = top.weight

        for v in graph[u]:
            if v.weight + w < dist[v.id]:
                dist[v.id] = w + v.weight
                pq.put(Node(v.id, dist[v.id]))


if __name__ == '__main__':
    N = int(input())
    E = int(input())
    T = int(input())
    M = int(input())

    for _ in range(M):
        u, v, w = map(int, input().split())
        graph[v].append(Node(u, w))
    Dijkstra(E)

    count = 0
    for i in range(1, N + 1):
        if dist[i] <= T:
            count += 1
    print(count)