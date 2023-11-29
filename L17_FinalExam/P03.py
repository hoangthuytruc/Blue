from math import sqrt
import queue
INF = 1e9


class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id

    def __lt__(self, other):
        return self.dist <= other.dist


def getDistance(x1, y1, x2, y2):
    return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

def prime(graph, src):
    n = len(graph)
    dist = [INF for _ in range(n)]
    visited = [False for _ in range(n)]

    pq = queue.PriorityQueue()
    pq.put(Node(src, 0))
    dist[src] = 0

    while not pq.empty():
        top = pq.get()
        u = top.id
        visited[u] = True
        for v in range(n):
            if not visited[v] and graph[u][v] < dist[v]:
                dist[v] = graph[u][v]
                pq.put(Node(v, dist[v]))
    total = 0
    for i in range(n):
        total += dist[i]
    return total


if __name__ == '__main__':
    tc = int(input())
    for k in range(tc):
        input()
        n = int(input())
        graph = [[] for _ in range(n)]
        nodes = []
        for i in range(n):
            x, y = map(float, input().split())
            nodes.append((x, y))

        for i in range(n):
            for j in range(n):
                d = getDistance(nodes[i][0], nodes[i][1], nodes[j][0], nodes[j][1])
                graph[i].append(d)
        if k > 0:
            print()
        print('{:.2f}'.format(prime(graph, 0)))