from queue import Queue

MAX = 1000 + 5

visited = [False] * MAX
length = [0] * MAX
graph = [[] for i in range(MAX)]


def BFS(s):
    q = Queue()
    visited[s] = True
    q.put(s)

    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                length[v] = length[u] + 1
                q.put(v)


if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        for i in range(MAX):
            visited[i] = False
            length[i] = 0
            graph[i].clear()

        V, E = map(int, input().split())
        for j in range(E):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)
        s = int(input())
        BFS(s)

        for i in range(1, V + 1):
            if i == s:
                continue

            print(length[i] * 6 if visited[i] else -1, end=' ')

        print()