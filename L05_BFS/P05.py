import queue

MAX = 100007
visited = [False] * MAX
graph = [[] for i in range(MAX)]
length = [0] * MAX


def BFS(s):
    q = queue.Queue()
    visited[s] = True
    q.put(s)
    length[s] = cat[s - 1]
    counter = 0

    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                if cat[v-1] == 1:
                    length[v] = length[u] + 1

                if length[v] <= maxCat:
                    if len(graph[v]) == 1:
                        counter += 1
                    else:
                        q.put(v)
    return counter


if __name__ == '__main__':
    n, maxCat = map(int, input().split())
    cat = list(map(int, input().split()))
    for i in range(1, n):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    print(BFS(1))