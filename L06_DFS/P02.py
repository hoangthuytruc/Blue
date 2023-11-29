def DFS(src):
    s = [src]
    visited[src] = True

    while len(s):
        u = s.pop()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                s.append(v)


if __name__ == '__main__':
    Q = int(input())
    for _ in range(Q):
        V = int(input())
        E = int(input())
        visited = [False for _ in range(V)]
        graph = [[] for _ in range(V)]
        for i in range(E):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)
        count = 0
        for i in range(V):
            if not visited[i]:
                count += 1
                DFS(i)
        print(count)