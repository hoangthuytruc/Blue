if __name__ == '__main__':
    arr = set()
    x_set = set()
    y_set = set()
    for i in range(8):
        a = tuple(map(int,input().split()))
        x_set.add(a[0])
        y_set.add(a[1])
        arr.add(a)
    if len(x_set) != 3 or len(y_set) != 3:
        print("ugly")
        exit()

    expected_set = set()
    x_set = list(sorted(x_set))
    y_set = list(sorted(y_set))

    for i in range(3):
       for j in range(3):
           if i == 1 and j == 1:
               continue
           else:
                expected_set.add((x_set[i], y_set[j]))

    if arr == expected_set:
        print("respectable")
    else:
        print("ugly")