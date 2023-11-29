from collections import deque

if __name__ == '__main__':
    case = 0
    while True:
        case += 1
        p, c = map(int, input().split())
        if p == 0 and c == 0:
            break
        else:
            print('Case {}:'.format(case))
            q = deque()
            for i in range(min(p, c)):
                q.append(i+1)
            for i in range(c):
                line = input().split()
                cmd = line[0]

                if cmd == "N":
                    print(q[0])
                    q.append(q.popleft())
                else:
                    x = int(line[1])
                    n = len(q)
                    q.append(x)
                    for i in range(n):
                        temp = q.popleft()
                        if temp != x:
                            q.append(temp)