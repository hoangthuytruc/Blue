import queue

MAX = 10001
INF = 1e9


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


def getIndex(s):
    for e in cities:
        if e[1] == s:
            return e[0]
    return -1


if __name__ == '__main__':
    Q = int(input())
    for _ in range(Q):
        E = int(input())
        graph = [[] for _ in range(E + 1)]
        cities = []
        for i in range(1, E + 1):
            city_name = input()
            cities.append((i, city_name))

            V = int(input())
            for j in range(V):
                u, w = map(int, input().split())
                graph[i].append(Node(u, w))
        t = int(input())
        for i in range(t):
            s, f = input().split()
            dist = [INF for _ in range(E + 1)]
            Dijkstra(getIndex(s))
            print(dist[getIndex(f)])
        _ = input()