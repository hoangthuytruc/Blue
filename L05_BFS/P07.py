import queue

dr = [0, -1, 1, 0]
dc = [1, 0, 0, -1]
MAX = 501
level = [None] * MAX


def BFS(sr, sc, fr, fc):
    q = queue.Queue()
    q.put((sr, sc))
    level[sr][sc] = 'X'

    while not q.empty():
        ur, uc = q.get()
        for i in range(4):
            r = ur + dr[i]
            c = uc + dc[i]
            if r == fr and c == fc and level[r][c] == 'X':
                return True
            if r in range(n) and c in range(m) and level[r][c] == '.':
                level[r][c] = 'X'
                q.put((r, c))
    return False


n, m = map(int, input().split())
for i in range(n):
    level[i] = list(input())
sr, sc = map(int, input().split())
fr, fc = map(int, input().split())
print("YES" if BFS(sr - 1, sc - 1, fr - 1, fc - 1) else "NO")