if __name__ == '__main__':
    n = int(input())
    points = list(map(int, input().split()))
    point_counter = {}
    for element in points:
        point_counter[element] = 0

    i = j = counter = max = 0

    while i < n and j < n:
        a = points[j]
        if point_counter[a] == 0:
            counter += 1
        point_counter[a] += 1

        if counter <= 2:
            if max < j - i:
                max = j - i
        while counter == 3:
            point_counter[points[i]] -= 1
            if point_counter[points[i]] == 0:
                counter -= 1
            i += 1
        j += 1
    print(max + 1)