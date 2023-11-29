if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()))

    l = r = 0
    sorted_array = sorted(array)

    for i in range(n):
        if array[i] != sorted_array[i]:
            l = i
            break
    for i in range(n - 1, -1, -1):
        if array[i] != sorted_array[i]:
            r = i
            break

    i, j = l, r
    while i < j:
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1

    if array != sorted_array:
        print("no")
        exit()

    print("yes")
    print(l + 1, r + 1)