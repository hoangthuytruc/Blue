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
    tc = int(input())
    for i in range(1, tc + 1):
        root = Node()
        n = int(input())
        is_consistent = False

        for _ in range(n):
            if not is_consistent:
                is_consistent = addWord(root, input())
            else:
                input()

        print('Case {}: {}'.format(i, 'NO' if is_consistent else 'YES'))

