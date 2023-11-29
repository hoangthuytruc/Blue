if __name__ == '__main__':
    n, a, b = map(int, input().split())
    complexities = list(map(int, input().split()))

    complexities.sort()
    chosen_complexity = complexities[b - 1]
    print(len(range(chosen_complexity, complexities[b])))