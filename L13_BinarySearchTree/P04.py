if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        setA = set(a[0:n])
        for c in a[n:n + m]:
            if c in setA:
                print("YES")
            else:
                setA.add(c)
                print("NO")