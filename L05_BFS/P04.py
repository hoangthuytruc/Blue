import queue


dr = [0, -1, 1, 0]
dc = [1, 0, 0, -1]
MAX = 21
visited = [[False] * MAX for _ in range(MAX)]
matrix = [None] * MAX


class Cell:
    def __init__(self, _r, _c):
        self.r = _r
        self.c = _c


def isBoundary(p: Cell) -> bool:
    if p.r == 0 or p.c == 0 or p.r == n - 1 or p.c == m - 1:
        return True
    else:
        return False


def isValid(r, c):
    return r in range(n) and c in range(m)


def BFS(s: Cell):
    q = queue.Queue()
    visited[s.r][s.c] = True
    q.put(s)
    counter = 1

    while not q.empty():
        u = q.get()
        for i in range(4):
            r = u.r + dr[i]
            c = u.c + dc[i]
            if isValid(r, c) and matrix[r][c] == '.' and not visited[r][c]:
                visited[r][c] = True
                q.put(Cell(r, c))
                counter += 1
    return counter


if __name__ == '__main__':
    tc = int(input())

    for x in range(tc):
        m, n = map(int, input().split())
        for i in range(n):
            matrix[i] = input()
        s = Cell(0, 0)
        for i in range(n):
            for j in range(m):
                visited[i][j] = False
                if matrix[i][j] == '@':
                    s = Cell(i, j)
        print("Case {:d}: {:d}".format(x+1, BFS(s)))