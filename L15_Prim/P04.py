import queue
INF = 1e9

class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id

    def __lt__(self, other):
        return self.dist <= other.dist

def prim(graph, src):
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
        for neighbor in graph[u]:
            v = neighbor.id
            w = neighbor.dist
            if not visited[v] and w < dist[v]:
                dist[v] = w
                pq.put(Node(v, w))

    total_cost = 0
    for i in range(n):
        if dist[i] >= INF:
            return "Impossible"
        total_cost += dist[i]
    return total_cost


if __name__ == '__main__':
    tc = int(input())
    for i in range(tc):
        input()
        m = int(input())
        graph = []
        cities = dict()
        cnt = 0
        for _ in range(m):
            c1, c2, w = input().split()
            if c1 in cities:
                u = cities[c1]
            else:
                u = cnt
                cities[c1] = u
                graph.append([])
                cnt += 1

            if c2 in cities:
                v = cities[c2]
            else:
                v = cnt
                cities[c2] = v
                graph.append([])
                cnt += 1
            graph[u].append(Node(v, int(w)))
            graph[v].append(Node(u, int(w)))
        print("Case {}: {}".format(i + 1, prim(graph, 0)))