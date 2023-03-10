T = int(input())
for test_case in range(1, T + 1):
    A, B = map(int, input().split())
    if A < 10 and B < 10:
        print(f'#{test_case} {A*B}')
    else:
        print(f'#{test_case} -1')