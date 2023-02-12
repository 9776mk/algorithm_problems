T = int(input())

for test_case in range(1,T+1):
    N = list(map(int, input().split()))
    print(f'#{test_case} {sum(N)/10:.0f}')