import queue
INF = 10 ** 9
energy = [0] * 105


class Edge:
    def __init__(self, _source, _target):
        self.source = _source
        self.target = _target


def hasPathBFS(s, f):
    visited = [False] * (n + 1)
    q = queue.Queue()
    q.put(s)
    visited[s] = True

    while not q.empty():
        u = q.get()

        for edge in graph:
            if edge.source == u:
                v = edge.target
                if not visited[v]:
                    visited[v] = True
                    q.put(v)
                if v == f:
                    return True
    return False


def BellmanFord(s, f):
    dist = [-INF] * (n + 1)
    dist[1] = 100

    for i in range(n - 1):
        for edge in graph:
            u = edge.source
            v = edge.target
            if dist[u] > 0:
                dist[v] = max(dist[v], dist[u] + energy[v])
    for edge in graph:
        u = edge.source
        v = edge.target

        if dist[u] > 0 and dist[u] + energy[v] > dist[v] and hasPathBFS(u, f):
            return True
    return dist[f] > 0


while True:
    n = int(input())
    if n == -1:
        break
    graph = []
    for u in range(1, n + 1):
        line = list(map(int, input().split()))
        energy[u] = line.pop(0)
        m = line.pop(0)
        for v in line:
            graph.append(Edge(u, v))
    canGo = BellmanFord(1, n)
    print("winnable" if canGo else "hopeless")