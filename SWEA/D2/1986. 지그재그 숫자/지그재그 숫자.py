T = int(input())

for test_case in range(1, T+1):
    sum = 0
    N = int(input())
    for i in range(1,N+1):
        if i%2!=0:
            sum += i
        else:
            sum -= i
    print(f'#{test_case} {sum}')

    