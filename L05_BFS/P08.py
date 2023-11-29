import queue

dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]
MAX = 251
matrix = [None] * MAX


def BFS(sr, sc):
    q = queue.Queue()
    q.put((sr, sc))
    sheep = 1 if matrix[sr][sc] == 'k' else 0
    wolf = 1 if matrix[sr][sc] == 'v' else 0
    matrix[sr][sc] = '#'

    canEscape = False

    while not q.empty():
        ur, uc = q.get()

        for i in range(4):
            r = ur + dr[i]
            c = uc + dc[i]

            if not (r in range(n) and c in range(m)):
                canEscape = True
                continue

            if matrix[r][c] != '#':
                sheep += 1 if matrix[r][c] == 'k' else 0
                wolf += 1 if matrix[r][c] == 'v' else 0
                q.put((r, c))
                matrix[r][c] = '#'
    if canEscape:
        return sheep, wolf
    elif sheep > wolf:
        return sheep, 0
    else:
        return 0, wolf


if __name__ == '__main__':
    n, m = map(int, input().split())
    sheeps = 0
    wolves = 0

    for i in range(n):
        matrix[i] = list(input())

    for i in range(n):
        for j in range(m):
            if matrix[i][j] != '#':
                total = BFS(i, j)
                sheeps += total[0]
                wolves += total[1]
    print(sheeps, wolves)