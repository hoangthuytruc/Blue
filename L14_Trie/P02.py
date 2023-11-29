class Node:
    def __init__(self):
        self.n_common = 0
        self.child = dict()


def addWord(root, s):
    global res
    tmp = root
    for i in range(len(s)):
        ch = s[i]
        level = i + 1
        if ch not in tmp.child:
            tmp.child[ch] = Node()
        tmp = tmp.child[ch]
        tmp.n_common += 1
        res = max(res, tmp.n_common * level)

if __name__ == '__main__':
    tc = int(input())
    for i in range(1, tc + 1):
        res = 0
        root = Node()
        n = int(input())
        for _ in range(n):
            s = input()
            addWord(root, s)
        print('Case {}: {}'.format(i, res))

