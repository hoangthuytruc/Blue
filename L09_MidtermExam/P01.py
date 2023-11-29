if __name__ == '__main__':
    Q = int(input())
    for _ in range(Q):
        n, m = map(int, input().split())
        s = list(map(int, input().split()))
        jobs = []
        for i in range(len(s)):
            jobs.append((i, s[i]))

        job = jobs[m]
        s.sort(reverse=True)
        time = 0
        max = s.pop(0)
        while True:
            top = jobs.pop(0)
            if max == top[1]:
                time += 1
                if top[1] == job[1] and top[0] == job[0]:
                    break
                else:
                    max = s.pop(0)
            else:
                jobs.append(top)
        print(time)