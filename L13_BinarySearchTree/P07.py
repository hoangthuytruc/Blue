if __name__ == '__main__':
    n = int(input())
    input()
    for i in range(n):
        trees = dict()
        cnt = 0
        res = []
        while True:
            t = input()
            if t.strip() == '':
                break
            cnt += 1
            if t in trees:
                trees[t] += 1
            else:
                trees[t] = 1

        for e in trees.keys():
            percent = trees[e] / cnt * 100
            res.append((e, percent))
        res.sort()
        for e in res:
            print('{} {:.4f}'.format(e[0], e[1]))
        if i < n - 1:
            print()