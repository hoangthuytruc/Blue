import queue
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

MAX = 1001
graph = [[0] * MAX for _ in range(MAX)]
visited = [[-1] * MAX for _ in range(MAX)]


def BFS(sr, sc):
    q = queue.Queue()
    q.put((sr, sc))

    while not q.empty():
        ur, uc = q.get()
        visited[ur][uc] = 0

        for i in range(4):
            r = ur + dr[i]
            c = uc + dc[i]

            if r in range(n) and c in range(m) and graph[r][c] == 0 and visited[r][c] == -1:
                visited[r][c] = visited[ur][uc] + 1
                q.put((r, c))


if __name__ == '__main__':
    n, m = map(int, input().split())
    k = int(input())
    for _ in range(k):
        line = input()
        for i in line[2:]:
            graph[int(line[0])][int(i)] = 1
    sr, sc = map(int, input().split())
    fr, fc = map(int, input().split())
    end = input()
    BFS(sr, sc)
    print(visited[fr][fc])


