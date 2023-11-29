import queue


def BFS(graph, src, rank):
    Q = queue.Queue()
    rank[src] = 0
    Q.put(src)
    while not Q.empty():
        u = Q.get()
        for v in graph[u]:
            if rank[v] == 'undefined':
                rank[v] = rank[u] + 1
                Q.put(v)
    return rank


if __name__ == '__main__':
    n = int(input())
    S = dict()
    cnt = 0
    graph = []
    for i in range(n):
        line = input().split()
        v = []
        for name in line:
            if name in S:
                id = S[name]
            else:
                S[name] = cnt
                id = cnt
                graph.append([])
                cnt += 1
            v.append(id)
        for x in v:
            for y in v:
                if x != y:
                    graph[x].append(y)
    rank = ['undefined' for _ in range(cnt)]
    if 'Isenbaev' in S:
        rank = BFS(graph, S['Isenbaev'], rank)
    a = []
    for name in S:
        a.append(name)
    a.sort()
    for name in a:
        print(name + ' ' + str(rank[S[name]]))
