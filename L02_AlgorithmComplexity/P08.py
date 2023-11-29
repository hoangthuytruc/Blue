def getLast(a) -> ():
    return a[len(a) - 1]


if __name__ == '__main__':
    n = int(input())
    consume_time = list(map(int, input().split()))
    if n == 1:
        print(consume_time[0], 0)
        exit()
    else:
        alice_consume_time = [(0, consume_time[0])]
        bob_consume_time = [(len(consume_time) - 1, consume_time[len(consume_time) - 1])]

        while len(alice_consume_time) + len(bob_consume_time) < n:
            a_lastElement = getLast(alice_consume_time)
            b_lastElement = getLast(bob_consume_time)
            if a_lastElement[1] <= b_lastElement[1]:
                nextIndex = a_lastElement[0] + 1
                alice_consume_time.append((nextIndex, a_lastElement[1] + consume_time[nextIndex]))
            else:
                nextIndex = b_lastElement[0] - 1
                bob_consume_time.append((nextIndex, b_lastElement[1] + consume_time[nextIndex]))
        print(len(alice_consume_time), len(bob_consume_time))