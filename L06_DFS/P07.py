import sys
sys.setrecursionlimit(5250000)
dr = [-1, 0, 0, 1, -1, 1, 1, -1]
dc = [0, -1, 1, 0, -1, -1, 1, 1]


def DFS(sr, sc):
    count = 0
    for i in range(8):
        r = sr + dr[i]
        c = sc + dc[i]

        if r in range(n) \
                and c in range(m) \
                and visited[r][c] == 0 \
                and ord(line[r][c]) - ord(line[sr][sc]) == 1:
            DFS(r, c)
            count = max(count, visited[r][c])
    visited[sr][sc] = count + 1
    return visited[sr][sc]


if __name__ == '__main__':
    Q = 0
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        Q += 1
        line = []
        visited = []
        for i in range(n):
            line.append(list(input()))
            visited.append([0] * m)
        res = 0
        for i in range(n):
            for j in range(m):
                if line[i][j] == 'A':
                    res = max(res, DFS(i, j))
        print("Case {}: {}".format(Q, res))
