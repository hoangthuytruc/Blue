if __name__ == '__main__':
    n, t = map(int, input().split())
    a = list(map(int, input().split()))

    i = j = time = count = 0
    for element in a:
        j += 1
        time += element
        if time > t:
            new_count = j - i
            if count < new_count:
                count = new_count
            time -= a[i]
            i += 1
    print(j - i)