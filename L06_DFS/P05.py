MAX = 10001
visited = [False for _ in range(MAX)]
graph = [[] for _ in range(MAX)]


def DFS(src):
    visited = [False] * (n+1)
    s = [src]
    visited[src] = True
    count = 0

    while len(s):
        u = s.pop()
        count += 1

        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                s.append(v)
    return count


if __name__ == '__main__':
    n, m = map(int, input().split())
    for i in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)

    max_bombs = 0
    for i in range(1, n+1):
        max_bombs = max(max_bombs, DFS(i))
    print(max_bombs)