import queue
MAX = 501
INF = int(1e9)


class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist

    def __lt__(self, other):
        return self.dist <= other.dist


def Dijkstra(s):
    pq = queue.PriorityQueue()
    pq.put(Node(s, 0))
    dist[s] = 0
    while not pq.empty():
        top = pq.get()
        u = top.id
        w = top.dist
        for neighbor in graph[u]:
            if w + neighbor.dist < dist[neighbor.id]:
                dist[neighbor.id] = w + neighbor.dist
                pq.put(Node(neighbor.id, dist[neighbor.id]))
                path[neighbor.id] = u


if __name__ == '__main__':
    E = int(input())
    graph = [[] for _ in range(MAX)]
    dist = [INF for _ in range(MAX)]
    path = [-1 for _ in range(MAX)]

    for i in range(E):
        u, v , w = map(int, input().split())
        graph[u].append(Node(v, w))
        graph[v].append(Node(u, w))
    s = int(input())
    Dijkstra(s)
    fs = int(input())
    for _ in range(fs):
        f = int(input())
        print(dist[f] if dist[f] != INF else "NO PATH")