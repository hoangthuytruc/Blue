if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            exit()
        else:
            cars = list(map(int, input().split()))
            waited_cars = []
            order = 1
            i = 0
            while i < n:
                if cars[i] == order:
                    order += 1
                    i += 1
                elif waited_cars and waited_cars[-1] == order:
                    order += 1
                    waited_cars.pop()
                else:
                    waited_cars.append(cars[i])
                    i += 1

            while waited_cars and waited_cars[-1] == order:
                order += 1
                waited_cars.pop()

            print('yes' if order == n + 1 else 'no')