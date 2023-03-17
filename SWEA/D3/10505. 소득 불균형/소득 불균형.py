# import sys

# sys.stdin = open("_소득불균형.txt")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    n_list = list(map(int, input().split()))
    avg_n = sum(n_list)/N
    cnt = 0

    for num in n_list:
        if num <= avg_n:
            cnt += 1
        else:
            continue

    print(f'#{test_case} {cnt}')