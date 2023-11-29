if __name__ == '__main__':
    k = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    total = 0
    count = 0
    for element in a:
        if total < k:
            total += element
            count += 1
        else:
            break
    if total < k:
        print(-1)
    else:
        print(count)