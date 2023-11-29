import queue

dr = [0, -1, 1, 0]
dc = [1, 0, 0, -1]
MAX = 21
visited = [[False] * MAX for _ in range(MAX)]
maze = [None] * MAX


class Point:
    def __init__(self, _r, _c):
        self.r = _r
        self.c = _c


def isBoundary(p: Point, m, n) -> bool:
    if p.r == 0 or p.c == 0 or p.r == m - 1 or p.c == n - 1:
        return True
    else:
        return False


def isValid(r, c, m, n):
    return r in range(m) and c in range(n)


def BFS(s: Point, f: Point, m, n):
    q = queue.Queue()
    visited[s.r][s.c] = True
    q.put(s)

    while not q.empty():
        u: Point = q.get()
        if u.r == f.r and u.c == f.c:
            return True

        for i in range(4):
            r = u.r + dr[i]
            c = u.c + dc[i]

            if isValid(r, c, m, n) and maze[r][c] == '.' and not visited[r][c]:
                visited[r][c] = True
                q.put(Point(r, c))

    return False


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        m, n = map(int, input().split())

        for i in range(m):
            maze[i] = input()
        gates = []
        for i in range(m):
            for j in range(n):
                visited[i][j] = False
                if maze[i][j] == '.' and isBoundary(Point(i, j), m, n):
                    gates.append(Point(i, j))

        if len(gates) != 2:
            print("invalid")
        else:
            s = gates[0]
            f = gates[1]
            print("valid" if BFS(s, f, m, n) else "invalid")