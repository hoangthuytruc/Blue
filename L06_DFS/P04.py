import sys
MAX = 10005
graph = [[] for _ in range(MAX)]
visited = [False for _ in range(MAX)]

sys.setrecursionlimit(10005)


def DFS(u):
    visited[u] = 1

    for v in graph[u]:
        if visited[v] == 1:
            return True

        elif visited[v] == 0:
            if DFS(v):
                return True

    visited[u] = 2
    return False


Q = int(input())
for _ in range(Q):
    n, m = map(int, input().split())
    for i in range(n+1):
        graph[i].clear()
        visited[i] = 0

    for i in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
    hasLoop = False
    for i in range(1, n+1):
        if visited[i] == 0:
            hasLoop = DFS(i)
            if hasLoop:
                break
    print("YES" if hasLoop else "NO")