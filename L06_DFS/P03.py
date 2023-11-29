dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
visited = [[False] * 51 for _ in range(51)]
lakes = []
matrix = []


def DFS(sr, sc):
    s = [(sr, sc)]
    visited[sr][sc] = True
    isOcean = False
    temp = []

    while len(s):
        ur, uc = s.pop()
        temp.append((ur, uc))

        if ur == 0 or uc == 0 or ur == n - 1 or uc == m - 1:
            isOcean = True

        for i in range(4):
            r = ur + dr[i]
            c = uc + dc[i]
            if r in range(n) and c in range(m) and matrix[r][c] == '.' and not visited[r][c]:
                visited[r][c] = True
                s.append((r, c))
    if not isOcean:
        lakes.append(temp)


if __name__ == '__main__':
    n, m, k = map(int, input().split())

    for i in range(n):
        matrix.append(list(input()))

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and matrix[i][j] == '.':
                DFS(i, j)

    lakes.sort(key=lambda lake: len(lake))
    sum = 0
    for i in range(len(lakes) - k):
        sum += len(lakes[i])
        for r, c in lakes[i]:
            matrix[r][c] = '*'
    print(sum)
    for i in range(n):
        print(''.join(matrix[i]))