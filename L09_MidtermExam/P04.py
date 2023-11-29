import queue


MAX = 201
V = None
E = None
visited = [False for _ in range(MAX)]
dist = [0 for _ in range(MAX)]
graph = [[] for _ in range(MAX)]


def canTransform(s,f):
    if len(s) != len(f):
        return False

    count = 0
    for i in range(len(s)):
        if s[i] != f[i]:
            count += 1
    return True if count == 1 else False


def BFS(s, f):
    visited = [False for _ in range(MAX)]
    dist = [-1 for _ in range(MAX)]
    q = queue.Queue()
    visited[s] = True
    dist[s] = 0
    q.put(s)

    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                dist[v] = dist[u] + 1
                q.put(v)
    return dist[f]


def getIndex(s):
    for w in dictionary:
        if w[1] == s:
            return w[0]
    return -1


if __name__ == '__main__':
    Q = int(input())
    input()
    for _ in range(Q):
        i = 0
        dictionary = []
        s = input()
        while s != '*':
            dictionary.append((i, s))
            i += 1
            s = input()

        for i in range(len(dictionary)):
            for j in range(len(dictionary)):
                if canTransform(dictionary[i][1], dictionary[j][1]):
                    graph[dictionary[i][0]].append(dictionary[j][0])

        t = input()
        while t.strip():
            w = t.split()
            print(w[0], w[1], BFS(getIndex(w[0]), getIndex(w[1])))
            try:
                t = input()
            except EOFError:
                break