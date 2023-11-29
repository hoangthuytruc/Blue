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
    edges = [{} for _ in range(n)]

    while not pq.empty():
        top = pq.get()
        u = top.id
        visited[u] = True
        for i in range(len(graph[u])):
            v = graph[u][i].id
            w = graph[u][i].dist
            if not visited[v] and w < dist[v]:
                dist[v] = w
                pq.put(Node(v, w))
                edges[v] = {'path': u, 'index': i}

    total_cost = 0
    for i in range(n):
        total_cost += dist[i]
    return total_cost, edges


if __name__ == '__main__':
    tc = int(input())
    for i in range(tc):
        n, m = map(int, input().split())
        graph = [[] for _ in range(n)]
        for _ in range(m):
            u, v, w = map(int, input().split())
            graph[u-1].append(Node(v-1, w))
            graph[v-1].append(Node(u-1, w))

        min1, edges = prim(graph, 0)
        min2 = INF
        for j in range(1, n):
            edge = edges[j]
            u = edge['path']
            i = edge['index']
            w = graph[u][i].dist
            graph[u][i].dist = INF
            cost, ith_edges = prim(graph, 0)
            graph[u][i].dist = w
            min2 = min(min2, cost)
        print(min1, min2)
