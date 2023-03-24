T = int(input())

change = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for test_case in range(1, T+1):
    N = int(input())
    list_ = []
    for money in change:
        list_.append(N // money)
        N %= money

    print(f'#{test_case}')
    for i in list_:
        print(i, end=' ')
    print()