if __name__ == '__main__':
    Q = int(input())
    for _ in range(Q):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))

        count = len(set(a))
        if count == k:
            print("Good")
        elif count > k:
            print("Average")
        else:
            print("Bad")