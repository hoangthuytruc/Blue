import queue

MAX = 100001


def BFS(s, f):
    dist = [-1] * MAX
    q = queue.Queue()
    q.put(s)
    dist[s] = 0

    while not q.empty():
        u = q.get()

        for x in a:
            v = (x * u) % 100000
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.put(v)

                if v == f:
                    return dist[v]
    return -1


if __name__ == '__main__':
    s, f = map(int, input().split())
    _ = int(input())
    a = list(map(int, input().split()))
    print(BFS(s, f))