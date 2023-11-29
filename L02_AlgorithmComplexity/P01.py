def findR(n, k, l, arr, count_arr) -> int:
    i = count = 0
    while i < n:
        if count_arr[arr[i]] == 0:
            count += 1
        count_arr[arr[i]] += 1
        if count < k:
            i += 1
        else:
            return i
    return -1


def findL(r, k, arr, count_arr) -> int:
    i = 0
    count = k
    while i < r:
        if count_arr[arr[i]] == 1:
            count -= 1
        count_arr[arr[i]] -= 1
        if count < k:
            return i
        else:
            i += 1
    return i


if __name__ == '__main__':
    n, k = map(int, input().split())
    array = list(map(int, input().split()))

    count_array = {}
    for element in array:
        count_array[element] = 0

    r = findR(n, k, 0, array, count_array)
    if r == -1:
        print(r, r)
    else:
        l = findL(r, k, array, count_array)
        print(l + 1, r + 1)