import sys

class Node:
    def __init__(self):
        self.end_word = False
        self.child = dict()


def addWord(root, s):
    tmp = root
    s_prefix_other = False
    other_prefix_s = True

    for ch in s:
        if ch not in tmp.child:
            tmp.child[ch] = Node()
            other_prefix_s = False

        tmp = tmp.child[ch]
        if tmp.end_word:
            s_prefix_other = True

    tmp.end_word = True
    return s_prefix_other or other_prefix_s

if __name__ == '__main__':
    n = int(input())
    root = Node()

    for _ in range(n):
        s = input()
        isPrefix = addWord(root, s)
        if isPrefix:
            print("BAD SET")
            print(s)
            sys.exit(0)
        else:
            continue
    print("GOOD SET")