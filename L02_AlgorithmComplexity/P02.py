if __name__ == '__main__':
    n, m = map(int, input().split())
    n_complexities = list(map(int, input().split()))
    m_complexities = list(map(int, input().split()))

    i = count = 0
    for j in range(m):
        if i == n:
            break

        if n_complexities[i] <= m_complexities[j]:
            count += 1
            i += 1
    print(n - count)