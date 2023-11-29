import sys
sys.setrecursionlimit(10000)
dr = [-1, 0, 0, 1, -1, 1, 1, -1]
dc = [0, -1, 1, 0, -1, -1, 1, 1]
sentence = "ALLIZZWELL"


def DFS(sr, sc, count):
    global hasPath, line, visited
    if count == len(sentence):
        hasPath = True
        return

    for i in range(8):
        r = sr + dr[i]
        c = sc + dc[i]

        if r in range(n) and c in range(m) and not visited[r][c] and line[r][c] == sentence[count]:
            visited[r][c] = True
            DFS(r, c, count + 1)
            visited[r][c] = False


if __name__ == '__main__':
    Q = int(input())
    for _ in range(Q):
        n, m = map(int, input().split())
        line = []
        visited = [[False] * m for _ in range(n)]

        for i in range(n):
            line.append(list(input()))
        _ = input()
        hasPath = False
        for i in range(n):
            for j in range(m):
                if line[i][j] == sentence[0] and not hasPath:
                    DFS(i, j, 1)
        print("YES" if hasPath else "NO")