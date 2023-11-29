MAX = 10001
V = None
E = None
visited = [False for _ in range(MAX)]
distance = [0 for _ in range(MAX)]
graph = [[] for _ in range(MAX)]


def DFS(src):
    for i in range(V):
        visited[i] = False
        distance[i] = 0
    s = []
    visited[src] = True
    s.append(src)

    while len(s) > 0:
        u = s.pop()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                s.append(v)
                distance[v] = distance[u] + 1


if __name__ == '__main__':
    V = int(input())
    for i in range(V - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    DFS(1)
    minID = (1001, 1001)
    Q = int(input())
    for _ in range(Q):
        girl = int(input())
        if distance[girl] < minID[0]:
            minID = distance[girl], girl
        if distance[girl] == minID[0] and minID[1] > girl:
            minID = minID[0], girl
    print(minID[1])